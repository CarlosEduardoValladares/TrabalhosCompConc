#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int N_threads;
int* vetor;

//variaveis do problema
int escrito = 0;
int somado = 0;
int iter = 0;

//variaveis para sincronizacao
pthread_mutex_t mutex_acesso;
pthread_cond_t cond_soma, cond_escrita, cond_iter;

void* funcao_thread(void* arg){

	int* endereco_meu_id = arg;
	int meu_id = *endereco_meu_id;
	int* somatorio = (int*) malloc(sizeof(int));
	*somatorio = 0;
	
	for(int i = 0; i < N_threads; i++){
	
		printf("Thread %d: Somando todo o vetor\n", meu_id);
		for(int j = 0; j < N_threads; j++){
		
			*somatorio += vetor[j];
		}
		
		pthread_mutex_lock(&mutex_acesso);
		somado++;
		if(somado < N_threads){
		
			printf("Thread %d: Aguardando as outras threads terminarem seus somatórios.\n", meu_id);			
			pthread_cond_wait(&cond_soma, & mutex_acesso);
			//printf("Saí do wait soma, id: %d\n", meu_id);

		} else {			
			printf("Thread %d: Último somatório feito. Liberando as Threads...\n", meu_id);
			somado = 0;
			pthread_cond_broadcast(&cond_soma);
			
		}

		pthread_mutex_unlock(&mutex_acesso);
		
		int aleatorio = ((int)rand())%10;
		pthread_cond_broadcast(&cond_soma);
		
		printf("Thread %d: Liberada da trava de soma! Escrevendo novo valor (%d) em Vetor[%d]\n",
				meu_id,
				aleatorio, 
				meu_id-1);
				
		vetor[meu_id-1] = aleatorio;
		pthread_mutex_lock(&mutex_acesso);
		escrito++;
		
		if(escrito < N_threads){
		
			printf("Thread %d: Aguardando as outras threads terminarem de escrever.\n", meu_id);
			pthread_cond_wait(&cond_escrita, &mutex_acesso);

		} else {			
			printf("Thread %d: Última escrita feita. Liberando as Threads...\n", meu_id);
			escrito = 0;
			pthread_cond_broadcast(&cond_escrita);
			
		}
		
		printf("Thread %d: Liberada da trava de escrita!.\n", meu_id);
		printf("Somatório parcial: %d\n", *somatorio);
		
		pthread_mutex_unlock(&mutex_acesso);
	}
	
	printf("Thread %d: Meu somatório final: %d\n", meu_id, *somatorio);
	pthread_exit( (void*) somatorio);

}

//funcao principal
int main(int argc, char* argv[]) {

  if(argc < 2){
  	printf("Chame o programa passando o Número de threads como argumento.\n");
  	printf("Ex: ./lab6.out 3");
  }
  
  N_threads = atoi(argv[1]);
  vetor = (int*) malloc(sizeof(int)*N_threads);
  int somatorio_final[N_threads];
  void* retorno = NULL;

  srand(time(0));
  
  puts("");
  printf("Disposição inicial do vetor:\n");
  for(int i = 0; i < N_threads; i++){
  
  	vetor[i] = ((int)rand())%10;
  	printf("Vetor[%d]: %d\n", i, vetor[i]);
  	
  }
  puts("");

  //identificadores das threads
  pthread_t tid[N_threads];
  int id[N_threads];

  //inicializa as variaveis de sincronizacao
  pthread_mutex_init(&mutex_acesso, NULL);
  pthread_cond_init(&cond_soma, NULL);
  pthread_cond_init(&cond_escrita, NULL);

  //cria as threads
  for(int i=0; i<N_threads; i++) {
  
    id[i] = i+1;
    if(pthread_create(&tid[i], NULL, funcao_thread, (void *) &id[i])) exit(-1);
  } 

  for(int i=0; i<N_threads; i++) {
  
		pthread_join(*(tid+i), &retorno);
		somatorio_final[i] = *((int*) retorno);
  }
  
  puts("");
  printf("Disposição final do vetor:\n");
  for(int i = 0; i < N_threads; i++){
  
  	printf("Vetor[%d]: %d\n", i, vetor[i]);
  	
  }
  puts("");
  
  printf("Disposição final dos somatorios:\n");
  for(int i = 0; i < N_threads; i++){
  
  	printf("somatorio[%d]: %d\n", i, somatorio_final[i]);
  	
  }
  puts("");
   
  return 0;
}
