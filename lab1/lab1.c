#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define TAMANHO 10000
#define N_THREADS 2

int vetor[TAMANHO];

// Função para avaliar corretude
int teste(int* lista){

	for(int i = 0; i < TAMANHO; i++){
		
		if(vetor[i] != i*i){
			printf("%d não é %d^2\n", vetor[i], i);
			return(-1);
		}
		
		/*
		Descomentando a linha abaixo, você pode
		verificar os valores finais 1 a 1 (em ordem)
		*/
		
		// printf("%d^2 = %d\n", i, vetor[i]);
	}

	return(0);

}

// Função para calcular os quadrados
// (generalizada para mais de 2 threads)
void *quadrado(void *args){

	int num = *((int*)args);

	// Cada thread calcula TAMANHO/N_THREADS valores
	for(int i = num; i < TAMANHO; i += N_THREADS){
		vetor[i] = i*i;
		
		/*
		Descomentando a linha abaixo, você pode
		verificar os valores sendo dinamicamente
		calculados
		*/
		
		// printf("%d^2 = %d\n", i, vetor[i]);	
		
	}
	
	// Liberando o ponteiro alocado para a 
	// passagem do parâmetro
	free(args);
	
	pthread_exit(NULL);

}

int main(){

	// Vetor com os n primeiros naturais
	for(int i = 0; i < TAMANHO; i++){
		vetor[i] = i;
	}
	
	int thread;
	pthread_t lista_threads[N_THREADS];
	
	for(thread = 0; thread < N_THREADS; thread++){
	
		// Argumento para guardar o inteiro a ser passado
		int *arg = malloc(sizeof(int));
		if(arg == NULL){
		
			printf("Erro: malloc()\n");
			exit(-1);
		
		}
		
		*arg = thread;
		
		int status;
		status = pthread_create(&lista_threads[thread], NULL, quadrado, (void*) arg);
		
		if(status != 0){
		
			printf("Erro: pthread_create()\n");
			exit(-1);
		
		}	
	}
	
	for(thread = 0; thread < N_THREADS; thread++){
	
		int status;
		status = pthread_join(lista_threads[thread], NULL);
		
		if(status != 0){
		
			printf("Erro: pthread_join()\n");
			exit(-1);
			
		}	
	}
	
	// Verifica se o vetor está com os valores finais corretos
	int status;
	status = teste(vetor);
	
	if(status != 0){
		
		printf("Falha do Teste\n");
		exit(-1);
		
	}
	
	printf("Teste Concluído, nenhum problema\n");
	
	return 0;

}
