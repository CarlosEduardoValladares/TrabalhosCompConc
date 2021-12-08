#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "timer.h"

long long int nElem; //dimensao do vetor de entrada
int nthreads; //numero de threads
float* vetor; //vetor de entrada com dimensao dim 
int respostaSeq, respostaConc;

typedef struct{
	int id;
	float infLim;
	float supLim;
} tArgs;

int initRand(float* vetor, int nElem){

	//preenche o vetor de entrada
	for(long long int i=0; i<nElem; i++){
	
	  vetor[i] = (float)rand()/((float)RAND_MAX);	  
	  
	}
	
	return 0;
}

int faixaSeq(float* vetor, float infLim, float supLim){

	int total = 0;
	for(long long int i = 0; i < nElem; i++){
	
		if( vetor[i] > infLim && vetor[i] < supLim){
			total++;
		}
	
	}
	
	printf("Valores entre %f e %f: %d (sequencial)\n", infLim, supLim, total);
	respostaSeq = total;
	return 0;
}

void* tarefa(void* arg){
	
	tArgs *args = (tArgs*) arg;
	int* qtd = (int*) malloc(sizeof(int));
	*qtd = 0;
	for(long long int i = args->id; i < nElem; i += nthreads){	
		if( (vetor[i] > args->infLim) && (vetor[i] < args->supLim)){
			*qtd = *qtd + 1;
			//printf("valor incluido: %f\n", vetor[i]);
		}
	
	}
	//printf("Valores nessa thread: %d\n", *qtd);
	//printf("Enereço enviado: %p\n", qtd);
	pthread_exit( (void*) qtd); 

}

int faixaConc(float* vetor, float infLim, float supLim){

	pthread_t *tid; //identificadores das threads no sistema
	tArgs *args;
	int total = 0;
	void* retorno = (void*) malloc(sizeof(int));
	
	if (nthreads > nElem) nthreads = nElem;
	
	tid = (pthread_t*) malloc(sizeof(pthread_t)*nthreads);	
    if(tid==NULL) {puts("ERRO--malloc"); return 2;}
    
    args = (tArgs*) malloc(sizeof(tArgs)*nthreads);
    if(args==NULL) {puts("ERRO--malloc"); return 2;}
    
    //cria threads
	for(int i = 0; i < nthreads; i++) {
	  (args+i)->id = i;
	  (args+i)->infLim = infLim;
	  (args+i)->supLim = supLim;
      if(pthread_create(tid+i, NULL, tarefa, (void*)(args+i))){
         puts("ERRO--pthread_create"); return 3;
      }
    }
    
	//espera pelo termino da threads
	for(int i=0; i<nthreads; i++) {
		pthread_join(*(tid+i), &retorno);
		//printf("endereço recebido: %p\n", retorno);
		total += *((int*)retorno);
	}   
	
	printf("Valores entre %f e %f: %d (concorrente)\n", infLim, supLim, total);
	respostaConc = total;
	return 0;
}

int main(int argc, char*argv[]){
	
	srand(time(0));

	if(argc < 3) {
	
       fprintf(stderr, "Digite: %s <numero de elementos> <numero threads>\n", argv[0]);
       return 1; 
       
    }
    
    float infLim, supLim;
	printf("Limite Inferior: ");
	scanf("%f", &infLim);
	printf("Limite Superior: ");
	scanf("%f", &supLim);
    
	nElem = atoll(argv[1]);
	nthreads = atoi(argv[2]);
	
	//aloca o vetor de entrada
	vetor = (float*) malloc(sizeof(float)*nElem);
	if(vetor == NULL) {
	
	  fprintf(stderr, "ERRO--malloc\n");
	  return 2;
	  
	}
	
	//inicializa o vetor
	if(initRand(vetor, nElem)){
	
	  fprintf(stderr, "ERRO--initRand\n");
	  return 3;

	}
	
	//os valores estão sendo gerados randomicamente entre 0 e 1
	/*for(int i=0; i<nElem; i++){
	
	  printf("%f ", vetor[i]);
	  
	}
	puts("");*/
	
	double inicio, fim, deltaConc, deltaSeq;
	puts("");
	//Chamada + Cálculo de tempo sequencial
	GET_TIME(inicio)
	if(faixaSeq(vetor, infLim, supLim)){
		
		fprintf(stderr, "ERRO--faixaSeq\n");
	    return 4;		
	    
	}
	GET_TIME(fim);
	deltaSeq = fim - inicio;
	printf("Tempo avaliação sequencial: %lf\n", deltaSeq);
	
	puts("");
	//Chamada + Cálculo de tempo concorrente
	GET_TIME(inicio)
	if(faixaConc(vetor, infLim, supLim)){
		
		fprintf(stderr, "ERRO--faixaConc\n");
	    return 5;		
	    
	}
	GET_TIME(fim);
	deltaConc = fim - inicio;
	printf("Tempo avaliação concorrente:%lf\n", deltaConc);
	
	puts("");
	if(respostaSeq == respostaConc){		
		printf("Resultados iguais!\n");
		
	} else {
		printf("Resultados diferentes!\n");
		
	}
	
	free(vetor);
	
	return 0;
}
