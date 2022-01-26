/* Disciplina: Computacao Concorrente */
/* Prof.: Silvana Rossetto */
/* Codigo: Leitores e escritores usando monitores em Java */
/* -------------------------------------------------------------------*/

// Monitor que implementa a logica do padrao leitores/escritores
class LE {
  private int leit, escr;  
  
  // Construtor
  LE() { 
     this.leit = 0; //leitores lendo (0 ou mais)
     this.escr = 0; //escritor escrevendo (0 ou 1)
  } 
  
  // Entrada para leitores
  public synchronized void EntraLeitor (int id) {
    try { 
      while (this.escr > 0) {
      //if (this.escr > 0) {
         System.out.println ("le.leitorBloqueado("+id+")");
         wait();  //bloqueia pela condicao logica da aplicacao 
      }
      this.leit++;  //registra que ha mais um leitor lendo
      System.out.println ("le.leitorLendo("+id+")");
    } catch (InterruptedException e) { }
  }
  
  // Saida para leitores
  public synchronized void SaiLeitor (int id) {
     this.leit--; //registra que um leitor saiu
     if (this.leit == 0) 
           this.notify(); //libera escritor (caso exista escritor bloqueado)
     System.out.println ("le.leitorSaindo("+id+")");
  }
  
  // Entrada para escritores
  public synchronized void EntraEscritor (int id) {
    try { 
      while ((this.leit > 0) || (this.escr > 0)) {
      //if ((this.leit > 0) || (this.escr > 0)) {
         System.out.println ("le.escritorBloqueado("+id+")");
         wait();  //bloqueia pela condicao logica da aplicacao 
      }
      this.escr++; //registra que ha um escritor escrevendo
      System.out.println ("le.escritorEscrevendo("+id+")");
    } catch (InterruptedException e) { }
  }
  
  // Saida para escritores
  public synchronized void SaiEscritor (int id) {
     this.escr--; //registra que o escritor saiu
     notifyAll(); //libera leitores e escritores (caso existam leitores ou escritores bloqueados)
     System.out.println ("le.escritorSaindo("+id+")");
  }
}



//Aplicacao de exemplo--------------------------------------------------------
class InteiroCompartilhado{

	private int inteiro;

	InteiroCompartilhado(int inteiro){
		this.inteiro = inteiro;
	
	}
	
	public void setInteiro(int valor){
		this.inteiro = valor;
	
	}
	
	public int getInteiro(){
		return this.inteiro;
		
	}

}

// Leitor
class Leitor extends Thread {
  int id; //identificador da thread
  int delay; //atraso bobo
  InteiroCompartilhado int_compartilhado;
  LE monitor;//objeto monitor para coordenar a lógica de execução das threads

  // Construtor
  Leitor (int id, InteiroCompartilhado int_compartilhado, LE m, int delay) {
    this.id = id;
    this.int_compartilhado = int_compartilhado;
    this.monitor = m;
    this.delay = delay;
  }

  // Método executado pela thread
  public void run () {
    //double j=777777777.7, i;
    try {
      while (true) {
        this.monitor.EntraLeitor(this.id);
        //for (i=0; i<100000000; i++) {j=j/2;} //...loop bobo para simbolizar o tempo de leitura
        if(this.int_compartilhado.getInteiro() % 2 == 0){
        	System.out.println("print('Thread Leitor - O inteiro lido é par: {0}'.format("+ this.int_compartilhado.getInteiro() +"))");
        	
        } else {
        	System.out.println("print('Thread Leitor - O inteiro lido é impar: {0}'.format("+ this.int_compartilhado.getInteiro() +"))");
        	
        }
        this.monitor.SaiLeitor(this.id);
        sleep(this.delay); 
      }
    } catch (Exception e) { return; }
  }
}

//--------------------------------------------------------
// Escritor
class Escritor extends Thread {
  int id; //identificador da thread
  int delay; //atraso bobo...
  InteiroCompartilhado int_compartilhado;
  LE monitor; //objeto monitor para coordenar a lógica de execução das threads

  // Construtor
  Escritor (int id, InteiroCompartilhado int_compartilhado, LE m, int delay) {
    this.id = id;
    this.int_compartilhado = int_compartilhado;
    this.monitor = m;
    this.delay = delay;
  }

  // Método executado pela thread
  public void run () {
    //double j=777777777.7, i;
    try {
      while (true) {
        this.monitor.EntraEscritor(this.id); 
        //for (i=0; i<100000000; i++) {j=j/2;} //...loop bobo para simbolizar o tempo de escrita
        System.out.println("print('Thread Escritor - Novo valor atribuído: {0}'.format(" + this.id + "))");
        this.int_compartilhado.setInteiro(this.id);
        this.monitor.SaiEscritor(this.id); 
        sleep(this.delay); //atraso bobo...
      }
    } catch (Exception e) { return; }
  }
}

//--------------------------------------------------------
// Escritor e Leitor
class Leitor_Escritor extends Thread {
  int id; //identificador da thread
  int delay; //atraso bobo...
  InteiroCompartilhado int_compartilhado;
  LE monitor; //objeto monitor para coordenar a lógica de execução das threads

  // Construtor
  Leitor_Escritor(int id, InteiroCompartilhado int_compartilhado, LE m, int delay) {
    this.id = id;
    this.int_compartilhado = int_compartilhado;
    this.monitor = m;
    this.delay = delay;
  }

  // Método executado pela thread
  public void run () {
    try {
      while (true) {
      
      	this.monitor.EntraLeitor(this.id);
      	int resultado = this.int_compartilhado.getInteiro();
      	System.out.println("print('Thread LeitorEscritor - O inteiro lido é: {0}'.format("+ resultado +"))");
        this.monitor.SaiLeitor(this.id);
        
        double j=777777777.7;
        for (int i=0; i<100000000; i++) {j=j/2;} //...loop bobo
        
        resultado++;
        this.monitor.EntraEscritor(this.id);         
        System.out.println("print('Thread LeitorEscritor - Novo valor atribuído: {0}'.format(" + resultado + "))");
        this.int_compartilhado.setInteiro(resultado);
        this.monitor.SaiEscritor(this.id); 
        sleep(this.delay); //atraso bobo...
      }
    } catch (Exception e) { return; }
  }
}

//--------------------------------------------------------
// Classe principal
class LeitorEscritor {
  static final int L = 4;
  static final int E = 3;
  static final int LeiEsc = 3;

  public static void main (String[] args) {
    int i;
    LE monitor = new LE();            // Monitor (objeto compartilhado entre leitores e escritores)
    Leitor[] l = new Leitor[L];       // Threads leitores
    Escritor[] e = new Escritor[E];   // Threads escritores
    Leitor_Escritor[] le = new Leitor_Escritor[LeiEsc]; // Threads leitores e escritores
    
    InteiroCompartilhado int_compartilhado = new InteiroCompartilhado(0);

    //inicia o log de saida
    System.out.println ("import verificaLE");
    System.out.println ("le = verificaLE.LE()");
    
    for (i=0; i<L; i++) {
       l[i] = new Leitor(i+1, int_compartilhado, monitor, 100);
       l[i].start(); 
    }
    for (i=0; i<E; i++) {
       e[i] = new Escritor(i+1, int_compartilhado, monitor, 100);
       e[i].start(); 
    }
    for (i=0; i<LeiEsc; i++) {
       le[i] = new Leitor_Escritor(i+1, int_compartilhado, monitor, 100);
       le[i].start(); 
    }
  }
}
