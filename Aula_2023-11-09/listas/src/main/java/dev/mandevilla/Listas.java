package dev.mandevilla;

import java.util.ArrayList;
import java.util.List;

public class Listas {
    public static void main(String[] args) {
        List<String> cidades = new ArrayList<>();

        // O add adiciona no final da lista
        cidades.add("Araguaína");
        cidades.add("Wanderlândia");
        cidades.add("Xambioa");
        cidades.add("Palmas");
        cidades.add("Gurupi");
        
        // O add com índice posiciona o elemento na posição desejada, e joga os demais valores para frente
        cidades.add(1, "Porto Nacional");
        cidades.add(4, "Formoso do Araguaína");

        // O set substitui o valor de uma determinada posição
        cidades.set(2, "Paraíso do Tocantins");

        // Remove o elemento de determinada posição e joga os demais valores para trás (não deixa o campo vazio)
        cidades.remove(3);

        // Remove o elemento pelo valor do próprio.
        cidades.remove("Gurupi");

        System.out.println("Apresentando cidades:");

        for (String cidade : cidades) {
            System.out.println(
                String.format("\t-> %s", cidade
            ));
        }

        int quantidadeCidades = cidades.size();

        System.out.println(
            String.format("\n%d cidades foram adicionadas.", quantidadeCidades)
        );

        String primeiraCidade = cidades.get(0);

        System.out.println("Primeira cidade da lista: " + primeiraCidade);
    }
}