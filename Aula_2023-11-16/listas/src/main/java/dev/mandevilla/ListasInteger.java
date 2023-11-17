package dev.mandevilla;

// Adicionando bibliotecas de Listas
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class ListasInteger {
    public static void main(String[] args) {
        System.out.println("-------------------------------------------------------------------------");

        // Criando a lista
        List<Integer> lista = new ArrayList<>();

        // Adicionando valores a lista (é adicionado ao fim da lista)
        lista.add(3);
        lista.add(6);
        lista.add(2023);
        lista.add(5);

        // Adicionando coleção
        lista.addAll(Arrays.asList(17, 1, 2005)); 

        // Adicionando no indíce informado
        lista.add(2, 17);        

        // Substituir elementos na lista
        lista.set(1, 23);

        // Remover elementos pelo indíce
        int elementoRemovido = lista.remove(4);
        System.out.println("Elemento removido: " + elementoRemovido);

        // Exibição da lista
        System.out.println("Elementos da lista: " + lista);

        // Exibição de elemento pelo indíce
        int elemento = lista.get(4);
        System.out.println("Exibindo elemento no indíce 4: " + elemento);

        // Exibindo a quantidade de elemntos que a lista possuí
        int tamanhoLista = lista.size();
        System.out.println(
            String.format(
                "Quantidade de elementos da lista: %d elementos",
                tamanhoLista
                ));
        
        // Verifica se contém determinado elemento na lista
        int elementoProcurar = 17;
        boolean elementoEncontrado = lista.contains(elementoProcurar);

        System.out.println(
            String.format(
                "Existe o elemento [%d] na lista: %s",
                elementoProcurar,
                elementoEncontrado
            )
        );

        // Verifica o indíce de um elemento passado
        int posicaoEncotrada = lista.indexOf(elementoProcurar);

        System.out.println(
            String.format(
                "Posição do elemento [%d] na lista: %d",
                elementoProcurar,
                posicaoEncotrada
            )
        );

        System.out.println("-------------------------------------------------------------------------");

        // Ordenar os valores da lista
        System.out.println("Lista original: " + lista);

        Collections.sort(lista);
        System.out.println("Lista crescente: " + lista);

        Collections.reverse(lista);
        System.out.println("Lista decrescente: " + lista);

        System.out.println("-------------------------------------------------------------------------");

        // Verificar se a lista está vazia
        boolean estaVazia = lista.isEmpty();
        System.out.println("Lista está vazia: " + estaVazia);

        // Limpar os valores da lista
        lista.clear();
        System.out.println("Lista está vazia: " + lista.isEmpty());
    }
}