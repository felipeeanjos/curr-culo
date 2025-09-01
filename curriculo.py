import streamlit as st


# Configuração da página
st.set_page_config(
    page_title="Currículo Felipe",
    page_icon="https://img.icons8.com/?size=100&id=23877&format=png&color=000000",
    layout="wide",
    initial_sidebar_state="expanded"
)


col1,col2 =st.columns([1,3])

with col1:
    st.image("https://i.imgur.com/dffziDo.jpeg", width=150)


with col2:
    st.markdown("<h1 style='color:black;'>Felipe dos Anjos</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:gray;'>Profissional de dados</h3>", unsafe_allow_html=True)

# Menu lateral
opcao = st.sidebar.selectbox("Escolha uma seção:", ["👤 Informações Pessoais", "🎓 Formação", "💼 Experiência", "🛠️ Habilidades"
                                                   # ,"📁 Projetos" 
                                                   ])

if opcao == "👤 Informações Pessoais":
    st.header("👤 Informações Pessoais")
    st.subheader("Sobre")
    st.write("""
Sou um profissional minucioso, com olhar analítico e foco em resultados. Acredito que decisões sólidas são construídas sobre dados confiáveis e interpretações precisas.

Por isso, me especializei em ferramentas essenciais para trabalhar com dados e automatizar processos, utilizando:

- **Excel / Google Sheets**: modelagem de dados, análises e estudos. 
- **Python**: tratamento, manipulação e visualização de grandes volumes de dados, além de automações eficientes.
- **Power BI**: desenvolvimento de relatórios dinâmicos e painéis interativos para tomada de decisão.
- **SQL (Snowflake)**: extração, consulta e organização estruturada de dados.
""")
    st.subheader("Contato")
    st.write("📍 Localização: Mogi das Cruzes, SP")
    st.write("📧 Email: felipemacedo_10@hotmail.com")
    st.write("📱 Telefone: (11) 96409-5102")
    

elif opcao == "🎓 Formação":
    st.header("🎓 Formação")
   
    st.write("""
    <strong>MBA, Inteligência de dados e Analytics para Negócios</strong> - Mackenzie
    <br><small style='color:gray; line-height:1;'>ago/2025 - Em progresso</small>
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Curso Livre Profissionalizante - Formação em dados</strong> - DNC
    <br><small style='color:gray; line-height:1;'>jan/2024 - jul/2024</small>
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Curso Livre Profissionalizante - Cientista de dados</strong> - EBAC
    <br><small style='color:gray; line-height:1;'>nov/2022 - nov/2023</small>
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Técnologo - Ciência de dados e análise de comportamento</strong> - Unicesumar
    <br><small style='color:gray; line-height:1;'>jan/2022 - nov/2023</small>
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Técnologo - Gestão Financeira</strong> - Unicesumar
    <br><small style='color:gray; line-height:1;'>fev/2018 - dez/2021</small>
    """, unsafe_allow_html=True)
    
    
elif opcao == '💼 Experiência':
    st.header("💼 Experiência")

    st.write("""
    <strong>Analista de S&OP</strong> - Martin Brower
    <br><small style='color:gray; line-height:1;'>nov/2024 - o momento </small> <br>
    Iniciei automatizando processos, validando bases de dados , fazendo estudos estratégicos de grandes volumes de dados com python e criando dashboards estratégicos para guiar as reuniões semanais de S&OE e mensais de S&OP , tive oportunidade de modelar / aperfeiçoar soluções de diarização da demanda para apoiar a operação (OUTBOUND), % de ocupação das docas (INBOUND) , BC's de novos clientes, projeção de ocupação dos CD's baseado na demanda, política de estoque e excedentes, estudo de otimização de transferências, avaliando todas essas frentes como um todo, e principalmente entendendo cada um dos processos da empresa.
    """, unsafe_allow_html=True)

    st.write("""
    <strong>🏆 Hackaton 1º lugar</strong> - EBAC em colab com Martin Brower
    <br><small style='color:gray; line-height:1;'>jan 2024 - 3 dias </small> <br>
    Fui o líder e responsável pela apresentação da solução, que se baseava em IA para solucionar o problema de gerenciamento de estoque da Martin Brower, quebrei uma barreira pessoal ao apresentar, me superei — e essa experiência foi decisiva para posteriormente ser contratado pela MB. <br>
    🔗 <a href="https://www.linkedin.com/feed/update/urn:li:activity:7134546054493945856/" target="_blank">Veja mais sobre essa experiência no meu LinkedIn</a>
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Analista de dados</strong> - Copa Família de fut7 (freelance)
    <br><small style='color:gray; line-height:1;'>abr/2024 - abr/2025 ¨ 1 ano 1 mês</small> <br>
    Tratamento de dados estatísticos com Google Sheets,python e Power BI. A copa família é um campeonato de futebol society fut7 ,onde todos os dados estatísticos da partida são documentados, como roubo de bola, assistências, gols, desarmes, interceptações e mais, todos esses dados são tratados pelas ferramentas ditas anteriormente e gerados insights e dashboards rodada a rodada.
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Cientista de dados</strong> - DNC (empresas parceiras)
    <br><small style='color:gray; line-height:1;'>jul/2024 - ago/2024 ¨ 2 meses</small> <br>
    Tive a oportunidade de participar de projetos em empresas parceiras a DNC, tratando dados reais, fazendo estudos estatísticos, correlação entre variáveis, criando modelos de machine learning como Random Forest com teste de R²  e desenvolvendo interfaces no streamlit como solução para deploy.
    
    """, unsafe_allow_html=True)

    st.write("""
    <strong>Auxiliar Administrativo</strong> - LEMAC comércio de bebidas
    <br><small style='color:gray; line-height:1;'>fev/2019 - fev/2022 ¨ 3 anos 1 mês</small> <br>
    Controle eficiente dos pedidos evitando erros e gerando eficiência e rapidez na entrega, atendimento ao cliente com foco em bom relacionamento, entendimento das rotas e análise e estudo de peços de compra e venda.
    """, unsafe_allow_html=True)


    

elif opcao == '🛠️ Habilidades' :
    st.subheader("🛠️ Habilidades")
    st.write("""
    <style>
        .skills-container {
            display: flex;
            justify-content: space-between;
            gap: 40px;
        }
        .column {
            width: 48%;
        }
        .skill-title {
            font-weight: bold;
            margin-bottom: 5px;
        }
        .stars {
            color: gold;
            font-size: 18px;
        }
        .skill {
            margin-bottom: 15px;
        }
    </style>

    <div class='skills-container'>
        <div class='column'>
            <h4>💻 Hard Skills</h4>
            <div class='skill'><span class='skill-title'>Python</span><br><span class='stars'>★★★★☆</span></div>
            <div class='skill'><span class='skill-title'>Power BI</span><br><span class='stars'>★★★★☆</span></div>
            <div class='skill'><span class='skill-title'>Excel</span><br><span class='stars'>★★★★☆</span></div>
            <div class='skill'><span class='skill-title'>SQL (snowflake)</span><br><span class='stars'>★★★★☆</span></div>
            <div class='skill'><span class='skill-title'>Visualização de dados</span><br><span class='stars'>★★★★★</span></div>
        </div>
        <div class='column'>
            <h4>🧠 Soft Skills</h4>
            <div class='skill'><span class='skill-title'>Visão de negócio</span><br><span class='stars'>★★★★★</span></div>
            <div class='skill'><span class='skill-title'>Resiliência</span><br><span class='stars'>★★★★★</span></div>
            <div class='skill'><span class='skill-title'>Inteligência emocional</span><br><span class='stars'>★★★★★</span></div>
            <div class='skill'><span class='skill-title'>Comunicação</span><br><span class='stars'>★★★★☆</span></div>
            <div class='skill'><span class='skill-title'>Resolução de Problemas</span><br><span class='stars'>★★★★★</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

#elif opcao == '📁 Projetos' :
    #st.subheader("📁 Projetos")