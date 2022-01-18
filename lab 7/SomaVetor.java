//classe da estrutura de dados (recurso) compartilhado entre as threads
class Sum {
  //recurso compartilhado
  private int valor;
  //construtor
  public Sum() { 
     this.valor = 0; 
  }

  public synchronized void add(int incremento) { 
     this.valor += incremento; 
  }

  public synchronized int get() { 
     return this.valor; 
  }
  
}

class IntArray {
  //recurso compartilhado
  private int[] vetor_interno;
  private int tamanho;
  //construtor
  public IntArray(int tamanho) {   
     this.vetor_interno = new int[tamanho];
     
     for(int i = 0; i < tamanho; i++){
     	this.vetor_interno[i] = i;		
     }
      
     this.tamanho = tamanho;
  }

  public synchronized int get(int pos) { 
     return this.vetor_interno[pos]; 
  }
  
  public synchronized int getSize() { 
     return this.tamanho; 
  }
  
}

class T implements Runnable {
   //identificador da thread
   private int id;
   private int qtd_threads;
   //objeto compartilhado com outras threads
   IntArray vetor_compartilhado;
   Sum somatorio;
  
   //construtor
   public T(int id, int qtd_threads, IntArray vetor, Sum somatorio) {
   	  this.id = id;
   	  this.qtd_threads = qtd_threads;
      this.vetor_compartilhado = vetor; 
      this.somatorio = somatorio;
   }

   //metodo main da thread
   public void run() {
      System.out.println("Thread " + this.id + " iniciou!");
      
      int soma_local = 0;
      int tam_vetor = this.vetor_compartilhado.getSize();
      
      for (int i = this.id; i < tam_vetor; i += this.qtd_threads) {
         soma_local += this.vetor_compartilhado.get(i);
           
      }      
      this.somatorio.add(soma_local);
      
      System.out.println("Thread " + this.id + " terminou!"); 
   }
}

//classe da aplicacao
class SomaVetor {

   static final int N_threads = 7;
   static final int Tam_vetor = 200;

   public static void main (String[] args) {
   
      //cria uma instancia do recurso compartilhado entre as threads
      IntArray vetor = new IntArray(Tam_vetor);
      Sum somatorio = new Sum();
      
      //reserva espaço para um vetor de threads
      Thread[] threads = new Thread[N_threads];

      //cria as threads da aplicacao
      for (int i = 0; i < threads.length; i++) {
         threads[i] = new Thread( new T(i, N_threads, vetor, somatorio));
      }

      //inicia as threads
      for (int i=0; i<threads.length; i++) {
         threads[i].start();
      }

      //espera pelo termino de todas as threads
      for (int i=0; i<threads.length; i++) {
         try { threads[i].join(); } catch (InterruptedException e) { return; }
      }

	  //Valor obtido pelo algoritmo de soma dinâmica pelas threads
      System.out.println("Valor de s = " + somatorio.get());
      
      //Valor obtido diretamente pela soma de P.A.: Sigma(inf=0, sup=n, var=i) = (n*(n-1))/2
      System.out.println("Valor esperado = " + (Tam_vetor * (Tam_vetor-1))/2 );
   }
}
