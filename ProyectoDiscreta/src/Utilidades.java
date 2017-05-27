
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Marlo
 */
public class Utilidades {

    ArrayList<String[]>aviones = new ArrayList<>();
    public void lector(){
        String archivo= "/Users/Marlo/NetBeansProjects/aviones.csv";
        BufferedReader br =null;
       try{
           String linea; 
           br = new BufferedReader(new FileReader(archivo));
           
           while((linea = br.readLine())!=null){
               aviones.add(linea.split(";"));
           }
       }
       catch(Exception ex){
           System.out.println("Error2");
       }
    
}
