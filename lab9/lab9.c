#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaforo_intermed, semaforo_final; // Semáforos a serem usados
int intermedOK = 0; // Contador das threads intermediárias

void* tarefa(void* arg){ // Função executada pelas threads

	int id = (*((int*) arg)) + 1;
	
	if(id == 5){
		printf("Seja bem-vindo!\n");
		
		for(int i = 0; i < 3; i++){// Thread 5 executou e vai liberar as 3 threads intermediárias
			sem_post(&semaforo_intermed);
		
		}
	
	} else if(id == 1){// Espera as threads intermediárias terminarem para imprimir
		sem_wait(&semaforo_final);
		printf("Volte sempre!\n");
	
	} else {
	
		sem_wait(&semaforo_intermed); // Espera a thread 5 executar para ser liberada
		switch(id){
		
			case 2:
				printf("Fique a vontade.\n");				
				break;
				
			case 3:
				printf("Sente-se por favor.\n");
				break;
				
			case 4:
				printf("Aceita um copo d’agua?\n");
				break;
		
		}
		intermedOK++;
		if(intermedOK == 3){// Se é a última thread intermediária, libera a thread final
			sem_post(&semaforo_final);
		
		}
	
	}
	
	return NULL;
} 

int main(){

	//Inicializa os Semáforos
	sem_init(&semaforo_intermed, 0, 0);
	sem_init(&semaforo_final, 0, 0);
	
	//Preparando parâmetros para pthread_create
	int** ids = (int**) malloc(sizeof(int*)*5);
	pthread_t* tid = (pthread_t*) malloc(sizeof(pthread_t)*5);
	
	//Cria as threads
	for(int i = 0; i < 5; i++){	
		int* pt = malloc(sizeof(int));	
		*pt = i;
		ids[i] = pt;
		
		if(pthread_create(tid+i, NULL, tarefa, (void*) ids[i])){
		     puts("ERRO--pthread_create"); return 3;
		     
		  }
	}
	
	//Espera as threads terminarem
	for(int i = 0; i < 5; i++) {
      pthread_join(*(tid+i), NULL);
      
   }

	return 0;
}
