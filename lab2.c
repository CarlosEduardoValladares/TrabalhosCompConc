/* Multiplicacao de matriz-matriz (considerando matrizes quadradas) */
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include "timer.h"

float *mat1; //matriz de entrada
float *mat2; //matriz de entrada
float *saida; //matriz de saida
float *saidaSequencial; //matriz de saida
int nthreads; //numero de threads

typedef struct{
   int id; //identificador do elemento que a thread ira processar
   int dim; //dimensao das estruturas de entrada
} tArgs;

//funcao que as threads executarao
void * tarefa(void *arg) {
   tArgs *args = (tArgs*) arg;
   //printf("Thread %d\n", args->id);
   for(int i=args->id; i<args->dim; i+=nthreads){
		for(int j=0; j<args->dim; j++){
			for(int k=0; k<args->dim; k++){
				
				saida[i*args->dim+j] += mat1[j*args->dim + k] * mat2[k*args->dim + j];
			
			}		
		}
	}
   pthread_exit(NULL);
}

void multSequencial(int dim){

	for(int i=0; i<dim; i++){
		for(int j=0; j<dim; j++){
			for(int k=0; k<dim; k++){
				
				saidaSequencial[i*dim+j] += mat1[j*dim + k] * mat2[k*dim + j];
			
			}		
		}
	}

}

void matrizesIguais(float* matriz1, float* matriz2, int dim){

	for(int i=0; i<dim; i++){
		for(int j=0; j<dim; j++){
			if(saida[i*dim+j] != saidaSequencial[i*dim+j]){
				puts("Matrizes Diferentes!\n");
				return;
			}	
		}
	}
	
	puts("Matrizes Iguais!\n");
	return;
}

//fluxo principal
int main(int argc, char* argv[]) {

   //seed aleatória para a rand()
   srand(time(0));


   int dim; //dimensao da matriz de entrada
   pthread_t *tid; //identificadores das threads no sistema
   tArgs *args; //identificadores locais das threads e dimensao
   double inicio, fim, deltaConc, deltaSeq;
   
   //GET_TIME(inicio);
   //leitura e avaliacao dos parametros de entrada
   if(argc<3) {
      printf("Digite: %s <dimensao da matriz> <numero de threads>\n", argv[0]);
      return 1;
   }
   dim = atoi(argv[1]);
   nthreads = atoi(argv[2]);
   if (nthreads > dim) nthreads=dim;

   //alocacao de memoria para as estruturas de dados
   mat1 = (float *) malloc(sizeof(float) * dim * dim);
   if (mat1 == NULL) {printf("ERRO--malloc\n"); return 2;}
   mat2 = (float *) malloc(sizeof(float) * dim * dim);
   if (mat2 == NULL) {printf("ERRO--malloc\n"); return 2;}
   saida = (float *) malloc(sizeof(float) * dim * dim);
   if (saida == NULL) {printf("ERRO--malloc\n"); return 2;}
   saidaSequencial = (float *) malloc(sizeof(float) * dim * dim);
   if (saidaSequencial == NULL) {printf("ERRO--malloc\n"); return 2;}

	
   //inicializacao das estruturas de dados de entrada e saida
   for(int i=0; i<dim; i++) {
      for(int j=0; j<dim; j++){
         mat1[i*dim+j] = (float)rand()/((float)RAND_MAX);
      	 mat2[i*dim+j] = (float)rand()/((float)RAND_MAX);
      	 saida[i*dim+j] = 0; 
      	 saidaSequencial[i*dim+j] = 0; 
      }
   }
   //GET_TIME(fim);
   //delta = fim - inicio;
   //printf("Tempo inicializacao:%lf\n", delta);

   //multiplicacao da matriz pelo vetor
   GET_TIME(inicio);
   //alocacao das estruturas
   tid = (pthread_t*) malloc(sizeof(pthread_t)*nthreads);
   if(tid==NULL) {puts("ERRO--malloc"); return 2;}
   args = (tArgs*) malloc(sizeof(tArgs)*nthreads);
   if(args==NULL) {puts("ERRO--malloc"); return 2;}
   //criacao das threads
   for(int i=0; i<nthreads; i++) {
      (args+i)->id = i;
      (args+i)->dim = dim;
      if(pthread_create(tid+i, NULL, tarefa, (void*) (args+i))){
         puts("ERRO--pthread_create"); return 3;
      }
   } 
   //espera pelo termino da threads
   for(int i=0; i<nthreads; i++) {
      pthread_join(*(tid+i), NULL);
   }
   GET_TIME(fim)   
   deltaConc = fim - inicio;
   printf("Tempo multiplicacao concorrente:%lf\n", deltaConc);

   //exibicao dos resultados
   
   /*puts("Matriz de saida:");
   for(int i=0; i<dim; i++){
      for(int j=0; j<dim; j++)
         printf("%lf ", saida[i*dim+j]);
   	  puts("");
   }*/
   
   GET_TIME(inicio)
   multSequencial(dim);
   GET_TIME(fim);
   deltaSeq = fim - inicio;
   printf("Tempo multiplicacao sequencial:%lf\n", deltaSeq);
   
   //matrizesIguais(saida, saidaSequencial, dim);
   /*puts("Matriz de saida:");
   for(int i=0; i<dim; i++){
      for(int j=0; j<dim; j++)
         printf("%lf ", saidaSequencial[i*dim+j]);
   	  puts("");
   }*/

   //liberacao da memoria
   //GET_TIME(inicio);
   free(mat1);
   free(mat2);
   free(saida);
   free(args);
   free(tid);
   //GET_TIME(fim)   
   //delta = fim - inicio;
   printf("Desempenho: %lf\n", deltaSeq/deltaConc);

   return 0;
}
