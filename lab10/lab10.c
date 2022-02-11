#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define tempo 0.25 * 1000000 //tempo do sleep
#define TAM 10

int buffer[TAM];
int qtd_itens;

sem_t mutex, libera, vazio;

void* produtor(void* arg){

	int id = *((int*) arg);
	while(1){
	
		printf("pc.produtorBloqueado(%d)\n", id);
		sem_wait(&vazio);
		
		//printf("print('Produtor %d: Enchendo o buffer...')\n", id);
		printf("pc.produtorProduzindo(%d)\n", id);
		printf("pc.setItens(%d)\n", TAM);
		
		//usleep(tempo);
		for(int i = 0; i < TAM; i++){
			buffer[i] = i+1;
		
		}
		
		qtd_itens = TAM;
		
		//printf("print('Produtor %d: Buffer cheio!')\n", id);
		printf("pc.produtorSaindo(%d)\n", id);
		//usleep(tempo);
		sem_post(&libera);
	
	}

	return NULL;

}

void* consumidor(void* arg){

	int id = *((int*) arg);

	while(1){	
		
		sem_wait(&mutex);
		
		if(qtd_itens != 0){
			//printf("print('Consumidor %d: Peguei o item %d')\n", id, buffer[qtd_itens-1]);
			printf("pc.consumidorConsumindo(%d)\n", id);
			//usleep(tempo);
			qtd_itens--;
		
		} else if (qtd_itens == 0){			
			qtd_itens--;
			sem_post(&vazio);
			printf("pc.consumidorBloqueado(%d)\n", id);
			sem_wait(&libera);
			printf("pc.consumidorSaindo(%d)\n", id);
		
		}
		
		sem_post(&mutex);
	
	}

	return NULL;

}

int main(int argc, char* argv[]){

	if(argc < 3){
	
		printf("Chame o arquivo como: ./{executável} {número_threads_produtoras} {número_threads_consumidoras} \n");
		return 1;
		
	}
	
	sem_init(&mutex, 0, 1);
	sem_init(&libera, 0, 0);
	sem_init(&vazio, 0, 0);
	qtd_itens = 0;
	
	int n_produtores = atoi(argv[1]);
	int n_consumidores = atoi(argv[2]);
	
	printf("import verificaPC\n");
	printf("pc = verificaPC.PC()\n");
	
	pthread_t tid[n_produtores + n_consumidores];

	for(int i = 0; i < n_produtores; i++){
	
		int* id = (int*) malloc(sizeof(int));
		*id = i+1;
		
		if(pthread_create(&tid[i], NULL, produtor, (void*) id)){
           puts("ERRO--pthread_create"); return 2;
         
      	}	
	}
	
	for(int i = 0; i < n_consumidores; i++){
	
		int* id = (int*) malloc(sizeof(int));
		*id = i+1;
	
		if(pthread_create(&tid[i + n_produtores], NULL, consumidor, (void*) id)){
           puts("ERRO--pthread_create"); return 2;
         
      	}	
	}
	
	for(int i = 0; i < TAM; i++) {
      pthread_join(*(tid+i), NULL);
      
   }

	return 0;
}
