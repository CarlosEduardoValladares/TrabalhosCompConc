#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <string.h>

#define N_THREADS 2
#define N_ELEMENTOS 100

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
	
	} else if( ((raiz -> filhoEsq) -> nFilhos) == 2 ){
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
int iteradorGlobal;
int iteradorRetorno;
int threads_dormindo;

pthread_mutex_t mutex_acesso, acessoGlobal, mutex_retorno, mutex_sono;
pthread_cond_t disponivel;

void DFS_concorrente(elemArv* arvore, int numero){

	if( (arvore -> valor) == numero ){
		printf("Valores batem!\n");
		
		printf("Adcionando retorno...\n");
		pthread_mutex_lock(&mutex_retorno);
		retornos[iteradorRetorno] = arvore;
		iteradorRetorno++;
		printf("Retorno adcionado!\n");
		pthread_mutex_unlock(&mutex_retorno);
	
	} else {
		printf("Valores não batem\n");
		
	}

	if( (arvore -> filhoDir) != NULL ){
	
		printf("Tem filho a direita...\n");
		ponteiroGlobal* elemFila = malloc(sizeof(ponteiroGlobal));
		elemFila -> subArvore = arvore -> filhoDir;
		elemFila -> checado = 0;
		
		printf("Colocando na fila global...\n");
		pthread_mutex_lock(&acessoGlobal);
		listaPonteiros[iteradorGlobal] = elemFila;
		iteradorGlobal++;
		printf("Colocado na fila global...\n");
		pthread_mutex_unlock(&acessoGlobal);
		printf("Acordando as dorminhocas...\n");
		pthread_cond_signal(&disponivel);		
	
	}
	
	if( (arvore -> filhoEsq) != NULL ){
		printf("Chamando recursivo DFS à esquerda...\n");
		DFS_concorrente(arvore -> filhoEsq, numero);
	
	}
	
	return;

}

void* tarefa(void* arg){

	int numero = ((tArgs*) arg) -> numero;
	int iteradorLocal = 0;
	
	pthread_mutex_lock(&mutex_acesso);
	while(iteradorLocal < N_ELEMENTOS){
		
		if( listaPonteiros[iteradorLocal] == NULL){
			printf("Fila vazia, dormindo...\n");
			pthread_mutex_lock(&mutex_sono);
			if(threads_dormindo == N_THREADS-1){
				printf("Todas as threads dormiram, sem mais trabalho! Encerrando...\n");
				pthread_mutex_unlock(&mutex_sono);
				threads_dormindo++;
				pthread_cond_broadcast(&disponivel);
				return NULL;
			}
			
			threads_dormindo++;
			pthread_mutex_unlock(&mutex_sono);
			pthread_cond_wait(&disponivel, &mutex_acesso);
			
			pthread_mutex_lock(&mutex_sono);
			if(threads_dormindo == N_THREADS){
				printf("Acordei e não tem mais trabalho! Encerrando...\n");
				return NULL;
			}
			
			printf("Acordei!\n");
			threads_dormindo--;
			pthread_mutex_unlock(&mutex_sono);			
			
		}
		
		pthread_mutex_unlock(&mutex_acesso);
		
		if( (listaPonteiros[iteradorLocal]) -> checado == 0){
			printf("Vértice não-checado! Analisando...\n");
			(listaPonteiros[iteradorLocal]) -> checado = 1;	
			printf("Chamando DFS...\n");
			DFS_concorrente((listaPonteiros[iteradorLocal]) -> subArvore, numero);
			printf("Retornei do DFS!\n");
			
		
		} else {
			printf("Vertice checado, indo pro próximo...\n");
			iteradorLocal++;
		
		}
	
	}
	
	printf("Terminei tudo!\n");	
	return NULL;

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
	printf("Caminho da raiz até o nó: %s\n", caminho);
	
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

	listaPonteiros = (ponteiroGlobal**) malloc(sizeof(ponteiroGlobal) * N_ELEMENTOS);
	retornos = (elemArv**) malloc(sizeof(elemArv) * N_ELEMENTOS);
	iteradorGlobal = 1;
	iteradorRetorno = 0;
	threads_dormindo = 0;

	elemArv* arvore = (elemArv*) malloc(sizeof(elemArv));
	arvore = initArv(arvore);
	
	for(int i = 0; i < N_ELEMENTOS; i++){
		insereArv(arvore, i);
	
	}
	
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
	
	// Thread
	
	pthread_t *tid; //identificadores das threads no sistema
	tArgs *args;
	
	tid = (pthread_t*) malloc(sizeof(pthread_t) * N_THREADS);	
    if(tid==NULL) {puts("ERRO--malloc"); return 2;}
    
    args = (tArgs*) malloc(sizeof(tArgs) * N_THREADS);
    if(args==NULL) {puts("ERRO--malloc"); return 2;}
    
    //cria threads
	for(int i = 0; i < N_THREADS; i++) {
	  (args+i)->id = i;
	  (args+i)->numero = numeroProcurado;
	  
	  printf("======= Início Log =======\n");
	  puts("");
      if(pthread_create(tid+i, NULL, tarefa, (void*)(args+i))){
         puts("ERRO--pthread_create"); return 3;
      }
    }
    
	//espera pelo termino da threads
	for(int i=0; i<N_THREADS; i++) {
		pthread_join(*(tid+i), NULL);
	}  
	printf("\n======= Fim Log =======\n"); 
	puts("");
	
	for(int i = 0; i < N_ELEMENTOS; i++){
		if(retornos[i] == NULL){
			break;
			
		}
		
		if(corretude(arvore, retornos[i], numeroProcurado) != 0){
			printf("Resultado incorreto, falha na corretude\n");
			return 0;
		}
	}
	
	printf("Corretude avaliada sem erros\n");
	
	return  0;

}
