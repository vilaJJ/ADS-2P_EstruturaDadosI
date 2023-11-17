package dev.mandevilla;

// Importando bibliotecas
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class ListasString {
    public static void main(String[] args) {
        System.out.println("-------------------------------------------------------------------------");

        // Criando a lista
        List<String> nomes = new ArrayList<>();

        // Adicionando valores a lista (é adicionado ao fim da lista)
        nomes.add("Juan Felipe Alves Flores");
        nomes.add("Bárbara Ohana Santos Silva");
        nomes.add("Maria Eduarda Batista de Souza");
        
        // Adicionando coleção
        nomes.addAll(Arrays.asList("Vitor Araújo dos Santos", "Beatriz Coelho dos Santos"));

        // Adicionando no indíce informado
        nomes.add(2, "Jefferson Ribeiro Vasconcelos Cunha");

        // Substituir elementos na lista
        nomes.set(3, "João Arthur Borges Rodrigues");

        // Remover elementos pelo indíce
        nomes.remove(4);

        // Exibição da lista
        System.out.println("Exibindo a lista de nomes:\n\t-> " + nomes);

        System.out.println("-------------------------------------------------------------------------");
        
        // Exibição de elemento pelo indíce
        int indiceElemento = 1;
        String elementoPeloIndice = nomes.get(indiceElemento);

        System.out.println(
            String.format(
                "Obtendo elemento pelo indíce %d:\n\t-> %s.",
                indiceElemento,
                elementoPeloIndice
            )
        );

        System.out.println("-------------------------------------------------------------------------");
        
        // Exibindo a quantidade de elemntos que a lista possuí
        int quantidadeElementos = nomes.size();

        System.out.println(
            String.format(
                "A lista possuí %d %s.",
                quantidadeElementos,
                quantidadeElementos == 1 ? "nome adicionado" : "nomes adicionados"
            )
        );

        System.out.println("-------------------------------------------------------------------------");
        
        // Verifica se contém determinado elemento na lista
        String elementoProcurar = "Joel Alburqueque";
        boolean existeElemento = nomes.contains(elementoProcurar);

        System.out.println(
            String.format(
                "O elemento '%s' %s na lista",
                elementoProcurar,
                existeElemento ? "existe" : "não existe"
            )
        );

        System.out.println("-------------------------------------------------------------------------");

        // Verifica o indíce de um elemento passado
        String elementoProcurarIndice = "Maria Eduarda Batista de Souza";
        int indiceElementoProcurar = nomes.indexOf(elementoProcurarIndice);

        System.out.println(
            String.format(
                "Indíce do elemento '%s':\n\t-> %d",
                elementoProcurarIndice,
                indiceElementoProcurar
            )
        );

        System.out.println("-------------------------------------------------------------------------");

        // Ordenar os valores da lista
        System.out.println("Lista original:\n\t-> " + nomes);

        Collections.sort(nomes);
        System.out.println("Lista crescrente:\n\t-> " + nomes);

        Collections.reverse(nomes);
        System.out.println("Lista decrescente:\n\t-> " + nomes);

        System.out.println("-------------------------------------------------------------------------");

        // Verificar se a lista está vazia
        boolean listaVazia = nomes.isEmpty();
        System.out.println("A lista está vazia:\n\t-> " + listaVazia);

        System.out.println("-------------------------------------------------------------------------");

        // Limpar os valores da lista
        nomes.clear();
        System.out.println("Lista depois do clear():\n\t-> " + nomes);

        System.out.println("-------------------------------------------------------------------------");
    }
}
