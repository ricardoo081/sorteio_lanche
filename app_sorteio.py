import streamlit as st
from processo import sortear_nomes

def main():
    st.title("Sorteio dos responsáveis pelo lanche (sexta-feira)")

    st.write("Insira os nomes separados por vírgula:")
    
    # Nomes pré-definidos
    nomes_predefinidos = "Ricardo, Cristiane, Arnaldo, Adilson, Adriana, Jake, Thayloan, Gabi, Raquel, Taynara, Rafael, Bianco"
    
    # Entrada de texto para os nomes com valores padrão
    nomes_input = st.text_area("Nomes", nomes_predefinidos)
    
    if st.button("Sortear"):
        # Converte a string de entrada em uma lista de nomes
        nomes = [nome.strip() for nome in nomes_input.split(",") if nome.strip()]
        
        if nomes:
            # Sorteia metade dos nomes, excluindo 'Ricardo'
            nomes_sorteados = sortear_nomes(nomes)
            
            st.write("Nomes sorteados:")
            for nome in nomes_sorteados:
                st.write(f"- {nome}")
            
            # Exibe o aviso
            st.warning("Atenção! Não trazer o lanche será considerado um crime... e você será expulso da sala!")
        else:
            st.write("Por favor, insira pelo menos um nome.")

if __name__ == "__main__":
    main()
