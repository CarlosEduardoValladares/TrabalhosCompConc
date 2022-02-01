#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <string.h>
#include "timer.h"

#define N_THREADS 4
#define N_ELEMENTOS 262144
// (2^18)-1

typedef struct elemArv elemArv;

struct elemArv{

	int nFilhos;
	int valor;
	elemArv* filhoEsq;
	elemArv* filhoDir; 
	elemArv* pai;

};

elemArv* initArv(elemArv* arvore){

	arvore -> nFilhos = 0;
	arvore -> valor = -1;
	arvore -> filhoEsq = NULL;
	arvore -> filhoDir = NULL;
	arvore -> pai = NULL;
	
	return arvore;

}

void insereArv(elemArv* raiz, int numero){

	if(raiz == NULL){
		printf("Vértice inválido\n");
		return;
	
	}
	
	if(raiz -> valor == -1){
		raiz -> valor = numero;
		return;
	
	} else if(raiz -> nFilhos == 0){
		elemArv* novoNo = (elemArv*) malloc(sizeof(elemArv));
		novoNo = initArv(novoNo);
		novoNo -> pai = raiz;
		
		novoNo -> valor = numero;
		raiz -> filhoEsq = novoNo;
		raiz -> nFilhos++;
		return;
	
	} else if(raiz -> nFilhos == 1){
		elemArv* novoNo = (elemArv*) malloc(sizeof(elemArv));
		novoNo = initArv(novoNo);
		novoNo -> pai = raiz;
		
		novoNo -> valor = numero;
		raiz -> filhoDir = novoNo;
		raiz -> nFilhos++;
		return;
	
	} else if( ((raiz -> filhoEsq) -> nFilhos) == 2){
		if ( ((raiz -> filhoDir) -> nFilhos) < 2 ){
			insereArv(raiz -> filhoDir, numero);
			return;	
			
		} else {
			insereArv(raiz -> filhoEsq, numero);
			return;			
		
		}
	
	} else {
		insereArv(raiz -> filhoEsq, numero);
		return;
		
	}

}

void preOrdem(elemArv* ptraiz){

	printf("%d ", (ptraiz) -> valor);
	if( ptraiz -> filhoEsq != NULL){
		preOrdem( ptraiz -> filhoEsq);
	}
	if( ptraiz -> filhoDir != NULL){
		preOrdem( ptraiz-> filhoDir);
	}
	return;

}



typedef struct{
	int numero;
	int id;
	
} tArgs;

typedef struct{
	elemArv* subArvore;
	int checado;
	
} ponteiroGlobal;

ponteiroGlobal** listaPonteiros;
elemArv** retornos;
elemArv** retornos_sequenciais;
int iteradorGlobal;
int iteradorRetorno;
int iteradorRetornoSeq;
int threads_dormindo;

pthread_mutex_t mutex_acesso, acessoGlobal, mutex_retorno, mutex_sono;
pthread_cond_t disponivel;

void DFS_concorrente(elemArv* arvore, int numero){

	if( (arvore -> valor) == numero ){
		//printf("Valores batem!\n");
		
		//printf("Adcionando retorno...\n");
		pthread_mutex_lock(&mutex_retorno);
		retornos[iteradorRetorno] = arvore;
		iteradorRetorno++;
		//printf("Retorno adcionado!\n");
		pthread_mutex_unlock(&mutex_retorno);
	
	} /*else {
		printf("Valores não batem\n");
		
	}*/

	if( (arvore -> filhoDir) != NULL ){
	
		//printf("Tem filho a direita...\n");
		ponteiroGlobal* elemFila = malloc(sizeof(ponteiroGlobal));
		elemFila -> subArvore = arvore -> filhoDir;
		elemFila -> checado = 0;
		
		//printf("Colocando na fila global...\n");
		pthread_mutex_lock(&acessoGlobal);
		listaPonteiros[iteradorGlobal] = elemFila;
		iteradorGlobal++;
		//printf("Colocado na fila global...\n");
		pthread_mutex_unlock(&acessoGlobal);
		//printf("Acordando as dorminhocas...\n");
		pthread_cond_signal(&disponivel);		
	
	}
	
	if( (arvore -> filhoEsq) != NULL ){
		//printf("Chamando recursivo DFS à esquerda...\n");
		DFS_concorrente(arvore -> filhoEsq, numero);
	
	}
	
	return;

}

void DFS_normal(elemArv* arvore, int numero){

	if( (arvore -> valor) == numero ){
		//printf("Valores batem!\n");
		
		//printf("Adcionando retorno...\n");
		retornos_sequenciais[iteradorRetornoSeq] = arvore;
		iteradorRetornoSeq++;
		//printf("Retorno adcionado!\n");
	
	} else {
		//printf("Valores não batem\n");
		
	}
	
	if( (arvore -> filhoEsq) != NULL ){
		//printf("Chamando recursivo DFS à esquerda...\n");
		DFS_normal(arvore -> filhoEsq, numero);
	
	}

	if( (arvore -> filhoDir) != NULL ){
	
		//printf("Chamando recursivo DFS à direita...\n");
		DFS_normal(arvore -> filhoDir, numero);		
	
	}
	
	return;

}

void* tarefa(void* arg){ //Thread lançada pela main
  int id = ((tArgs*) arg) -> id; //Armazena seu id
  int numero = ((tArgs*) arg) -> numero; //Armazena o número do vértice que estamos buscando
  int iteradorLocal = 0; //Mantém um iterador para percorrer pela fila
  
  pthread_mutex_lock(&mutex_acesso); //Faz um lock para acessar a variável global
  while(iteradorLocal < N_ELEMENTOS){ //Verifica se já não fez o máximo de iterações
    
    if( listaPonteiros[iteradorLocal] == NULL){ //Caso não haja nenhuma sub-árvore para ser lida
      //printf("Fila vazia, dormindo... - Disse %d\n", id);
      pthread_mutex_lock(&mutex_sono); //Faz um lock para verificar quantas threads estão ociosas
      if(threads_dormindo == N_THREADS-1){ //Caso todas execeto essa estejam ociosas
        //printf("Todas as threads dormiram, sem mais trabalho! Encerrando... - Disse %d\n", id);
        threads_dormindo++;
        pthread_cond_broadcast(&disponivel); //Libera todas as outras threads
                pthread_mutex_unlock(&mutex_acesso);
        pthread_mutex_unlock(&mutex_sono);
        return NULL; //Encerra seu processamento
      }
      
      threads_dormindo++; //Aumenta o número de threads "dormindo"

      pthread_mutex_unlock(&mutex_sono);

      //printf("indo dormir - Disse %d\n", id);

      pthread_cond_wait(&disponivel, &mutex_acesso); //Fica ociosa, aguardando alguma nova sub-árvore não explorada ou o fim da execução

      //printf("acordando - Disse %d\n", id);

      pthread_mutex_lock(&mutex_sono);

      if(threads_dormindo == N_THREADS){ //Caso todas as threads estejam ociosas
        //printf("Acordei e não tem mais trabalho! Encerrando... - Disse %d\n", id);
        ////pthread_cond_broadcast(&disponivel); //Libera alguma possível thread ociosa
                pthread_mutex_unlock(&mutex_acesso);
        pthread_mutex_unlock(&mutex_sono);
        return NULL; //Encerra seu processamento
      }
      
      //printf("Acordei!\n");
      threads_dormindo--; //Sai da contagem de threads ociosas, para verificas se há alguma sub-árvore que possa executar o DFS
      pthread_mutex_unlock(&mutex_sono);      
      
    }
    
    pthread_mutex_unlock(&mutex_acesso);
    
    if( (listaPonteiros[iteradorLocal]) -> checado == 0){ //Caso a sub-árvore ainda não tenha sido verificada
      //printf("Vértice não-checado! Analisando...\n");
      (listaPonteiros[iteradorLocal]) -> checado = 1;  
      //printf("Chamando DFS...\n");
      DFS_concorrente((listaPonteiros[iteradorLocal]) -> subArvore, numero);
      //printf("Retornei do DFS!\n");
      
    
    } else {
      //printf("Vertice checado, indo pro próximo...\n");
      iteradorLocal++;
    
    }

        pthread_mutex_lock(&mutex_acesso);
  
  }
  
  //printf("Terminei tudo!\n");  
  return NULL; //Encerra seu processamento

}

char* recuperaCaminho(elemArv* no, char* stringCaminho){

	elemArv* pai = no -> pai;
	
	if(pai == NULL){
		return stringCaminho;
	
	}
	
	if(pai -> filhoEsq == no){
		char ch = 'e';
		strncat(stringCaminho, &ch, 1);
		recuperaCaminho(pai, stringCaminho);
	
	}
	
	if(pai -> filhoDir == no){
		char ch = 'd';
		strncat(stringCaminho, &ch, 1);
		recuperaCaminho(pai, stringCaminho);
	
	}
	
	return stringCaminho;

}

char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}

int corretude(elemArv* arvore, elemArv* retorno, int numero){

	char* caminho = (char*) malloc(sizeof(char)*N_ELEMENTOS);
	recuperaCaminho(retorno, caminho);
	
	caminho = strrev(caminho);
	//printf("Caminho da raiz até o nó: %s\n", caminho);
	
	int tamanho = strlen(caminho);
	for(int i = 0; i < tamanho; i++){
		if (caminho[i] == 'e'){
			arvore = arvore -> filhoEsq;
		
		}
		
		if(caminho[i] == 'd'){
			arvore = arvore -> filhoDir;
		
		}
	
	}
	
	if(arvore->valor == numero){	
		return 0;
	
	} else{
		return 1;
			
	}
		
	return 1;

}

int main(){

	double inicio, fim, deltaConc, deltaSeq;

	listaPonteiros = (ponteiroGlobal**) malloc(sizeof(ponteiroGlobal) * N_ELEMENTOS);
	retornos = (elemArv**) malloc(sizeof(elemArv) * N_ELEMENTOS);
	retornos_sequenciais = (elemArv**) malloc(sizeof(elemArv) * N_ELEMENTOS);
	iteradorGlobal = 1;
	iteradorRetorno = 0;
	iteradorRetornoSeq = 0;
	threads_dormindo = 0;

	elemArv* arvore = (elemArv*) malloc(sizeof(elemArv));
	arvore = initArv(arvore);
	
	GET_TIME(inicio);
	for(int i = 0; i < N_ELEMENTOS; i++){
		insereArv(arvore, i);
	
	}
	GET_TIME(fim);
	
	deltaSeq = fim - inicio;
	printf("Tempo inserção: %lfs\n", deltaSeq);
	
	//preOrdem(arvore);
	//puts("");
	
	//Vértice inicial
	ponteiroGlobal* ptInit = malloc(sizeof(ponteiroGlobal));
	ptInit -> subArvore = arvore;
	ptInit -> checado = 0;
	
	listaPonteiros[0] = ptInit;
	
	//printf("%p\n", (listaPonteiros));
	//printf("%p\n", (listaPonteiros[0]) -> subArvore);
	//printf("%d\n", (listaPonteiros[0]) -> checado);
	
	int numeroProcurado;
	printf("Digite o número a ser buscado: ");
	scanf("%d", &numeroProcurado);
	puts("");
	
	// DFS Sequencial - Início
	GET_TIME(inicio);
	DFS_normal(arvore, numeroProcurado);
	GET_TIME(fim);
	// DFS Sequencial - Fim
	
	deltaSeq = fim - inicio;
	printf("Tempo busca sequencial: %lfs\n", deltaSeq);
	
	// DFS Concorrente - Início
	GET_TIME(inicio);
	pthread_t *tid; //identificadores das threads no sistema
	tArgs *args;
	
	tid = (pthread_t*) malloc(sizeof(pthread_t) * N_THREADS);	
    if(tid==NULL) {puts("ERRO--malloc"); return 2;}
    
    args = (tArgs*) malloc(sizeof(tArgs) * N_THREADS);
    if(args==NULL) {puts("ERRO--malloc"); return 2;}
    
    //printf("======= Início Log =======\n");
	puts("");
    //cria threads
	for(int i = 0; i < N_THREADS; i++) {
	  (args+i)->id = i;
	  (args+i)->numero = numeroProcurado;

      if(pthread_create(tid+i, NULL, tarefa, (void*)(args+i))){
         puts("ERRO--pthread_create"); return 3;
      }
    }
    
	//espera pelo termino da threads
	for(int i=0; i<N_THREADS; i++) {
		pthread_join(*(tid+i), NULL);
	}  
	//printf("\n======= Fim Log =======\n"); 
	//puts("");
	GET_TIME(fim);
	// DFS Concorrente - Fim
	
	deltaConc = fim - inicio;
	printf("Tempo busca concorrente: %lfs\n", deltaConc);
	puts("");
	
	//Corretude Sequencial
	for(int i = 0; i < N_ELEMENTOS; i++){
		if(retornos_sequenciais[i] == NULL){
			break;
			
		}
		
		if(corretude(arvore, retornos_sequenciais[i], numeroProcurado) != 0){
			printf("Resultado incorreto, falha na corretude\n");
			return 0;
		}
	}
	
	printf("Corretude sequencial avaliada sem erros\n");
	puts("");
	
	//Corretude Concorrente
	for(int i = 0; i < N_ELEMENTOS; i++){
		if(retornos[i] == NULL){
			break;
			
		}
		
		if(corretude(arvore, retornos[i], numeroProcurado) != 0){
			printf("Resultado incorreto, falha na corretude\n");
			return 0;
		}
	}
	
	printf("Corretude concorrente avaliada sem erros\n");
	puts("");
	
	printf("Desempenho: %lf\n", deltaSeq/deltaConc);
	puts("");
	
	return  0;

}
