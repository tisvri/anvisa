import streamlit as st
import pandas as pd
import plotly_express as px

#TODO
#   Criar Colunas;
#   Fazer Filtro (Global) contido em siderbar;
#   Criar sessions_states e callbacks

if 'patrocinadores' not in st.session_state:
    st.session_state['patrocinadores'] = []
if 'tipo_estudo' not in st.session_state:
    st.session_state['tipo_estudo'] = []
if 'tipo_medicamento' not in st.session_state:
    st.session_state['tipo_medicamento'] = []
if 'nome_medicamento' not in st.session_state:
    st.session_state['nome_medicamento'] = []
if 'classe_terapeutica' not in st.session_state:
    st.session_state['classe_terapeutica'] = []
if 'situacao_estudo' not in st.session_state:
    st.session_state['situacao_estudo'] = []


@st.cache_data
def load_anvisa_df():
    df = pd.read_csv('anvisa_filtered.csv', encoding='utf8')
    if "Unnamed" in df.columns.to_list():
        df.drop(columns=['Unnamed'])
    return df

def filter_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    if st.session_state['patrocinadores']:
        dataframe = dataframe[dataframe['Patrocinador do Estudo'].isin(st.session_state['patrocinadores'])]
    if st.session_state['tipo_estudo']:
        dataframe = dataframe[dataframe['Tipo de Estudo'].isin(st.session_state['tipo_estudo'])]
    if st.session_state['tipo_medicamento']:
        dataframe = dataframe[dataframe['Tipo de Medicamento Experimental'].isin(st.session_state['tipo_medicamento'])]
    if st.session_state['nome_medicamento']:
        dataframe = dataframe[dataframe['Nome ou Código do Medicamento Experimental'].isin(st.session_state['nome_medicamento'])]
    if st.session_state['classe_terapeutica']:
        dataframe = dataframe[dataframe['Classe Terapêutica'].isin(st.session_state['classe_terapeutica'])]
    if st.session_state['situacao_estudo']:
        dataframe = dataframe[dataframe['Situação do Estudo'].isin(st.session_state['situacao_estudo'])]
    
    return dataframe

#############################################################################################################
anvisa_df = load_anvisa_df()

col1,col2 = st.columns(2, vertical_alignment='center')
# col1,col2 = st.columns([2,2])
############################################################
# pie = anvisa_df.groupby('Situação do Estudo')['Número do Processo'].nunique().reset_index()

# piechart = px.pie(
#     pie,
#     values='Número do Processo',
#     names='Situação do Estudo',
#     title=r'% da Situações dos Estudos'
# )

# piechart.update_layout(showlegend=False)
# #############################################################

# v_bar = anvisa_df.groupby('Patrocinador do Estudo')['Número do Processo'].size().reset_index().sort_values(by='Número do Processo', ascending=False)
# v_bar = v_bar.head(40)
# vertical_bar = px.bar(
#     v_bar,
#     orientation='h',
#     x='Número do Processo',
#     y='Patrocinador do Estudo',
#     color='Patrocinador do Estudo',
#     title='Total por Patrocinador'
# )

# vertical_bar.update_layout(showlegend=False)

# pie_drug = anvisa_df.groupby('Tipo de Medicamento Experimental')['Número do Processo'].size().reset_index().sort_values(by='Número do Processo', ascending=False)

# pie_drug_chart = px.bar(
#     pie_drug,
#     orientation='h',
#     x='Número do Processo',
#     y='Tipo de Medicamento Experimental',
#     color='Tipo de Medicamento Experimental',
#     title='Total por Tipo de Medicamento Experimental'
# )

# pie_drug_chart.update_layout(showlegend=False)

# bar_class = anvisa_df.groupby('Classe Terapêutica')['Número do Processo'].size().reset_index().sort_values(by='Número do Processo', ascending=False)
# bar_class = bar_class.head(5)

# bar_class_chart = px.bar(
#     bar_class,
#     orientation='h',
#     x='Número do Processo',
#     y='Classe Terapêutica',
#     color='Classe Terapêutica',
#     title='Total por Classe Terapêutica'
# )

# bar_class_chart.update_layout(showlegend=False)

# pie_estudo = anvisa_df.groupby("Tipo de Estudo")["Número do Processo"].nunique().reset_index()

# pie_estudo_chart = px.pie(
#     pie_estudo,
#     names="Tipo de Estudo",
#     values="Número do Processo",
#     title='% Tipo de Estudo'
# )

# pie_estudo_chart.update_layout(showlegend=False)

# with col1:
#     st.plotly_chart(piechart)
#     st.plotly_chart(bar_class_chart)

# with col2:
#     st.plotly_chart(pie_drug_chart)
#     st.plotly_chart(pie_estudo_chart)

# # with col3:
# #     st.plotly_chart(vertical_bar)

# st.plotly_chart(vertical_bar)

# st.dataframe(
#     anvisa_df[['Patrocinador do Estudo', 'Nome ou Código do Medicamento Experimental', 'Tipo de Medicamento Experimental', 'Doença', 'Fase do Estudo', 'Situação do Estudo']],
#     column_config= 
#     {
#         'Número do Processo': st.column_config.TextColumn()
#     }
#     )

#TODO Fazer Função para esse sidebar
with st.sidebar:
    st.title('Filtros:')

    
    # Patrocinador do Estudo
    with st.expander('Patrocinador do Estudo'):
        sponsors = st.multiselect(
            label='Filtro Multiseleção',
            options=anvisa_df['Patrocinador do Estudo'].unique().tolist(),
            placeholder='Selecione Um ou Vários Valores:'
        )
        st.session_state['patrocinadores'] = sponsors
    
    # Tipo de Estudo
    with st.expander('Tipo de Estudo'):
        tipos_estudo = st.multiselect(
            label='Filtro Multiseleção',
            options=anvisa_df['Tipo de Estudo'].unique().tolist(),
            placeholder='Selecione Um ou Vários Valores:'
        )
        st.session_state['tipo_estudo'] = tipos_estudo
    
    # Situação do Estudo
    with st.expander('Situação do Estudo'):
        situacao_estudo = st.multiselect(
            label='Filtro Multiseleção',
            options=anvisa_df['Situação do Estudo'].unique().tolist(),
            placeholder='Selecione Um ou Vários Valores:'
        )
        
        st.session_state['situacao_estudo'] = situacao_estudo

    # Tipo de Medicamento Experimental
    with st.expander('Tipo de Medicamento Experimental'):
        tipos_medicamento = st.multiselect(
            label='Filtro Multiseleção',
            options=anvisa_df['Tipo de Medicamento Experimental'].unique().tolist(),
            placeholder='Selecione Um ou Vários Valores:'
        )
        st.session_state['tipo_medicamento'] = tipos_medicamento

    # Nome ou Código do Medicamento Experimental
    with st.expander('Nome ou Código do Medicamento Experimental'):
        nomes_medicamento = st.multiselect(
            label='Filtro Multiseleção',
            options=anvisa_df['Nome ou Código do Medicamento Experimental'].unique().tolist(),
            placeholder='Selecione Um ou Vários Valores:'
        )
        st.session_state['nome_medicamento'] = nomes_medicamento

    # Classe Terapêutica
    with st.expander('Classe Terapêutica'):
        classes_terapeuticas = st.multiselect(
            label='Filtro Multiseleção',
            options=anvisa_df['Classe Terapêutica'].unique().tolist(),
            placeholder='Selecione Um ou Vários Valores'
        )
        st.session_state['classe_terapeutica'] = classes_terapeuticas

# st.write(st.session_state)
anvisa_df = filter_dataframe(anvisa_df)

pie = anvisa_df.groupby('Situação do Estudo')['Número do Processo'].nunique().reset_index()

piechart = px.pie(
    pie,
    values='Número do Processo',
    names='Situação do Estudo',
    title=r'% da Situações dos Estudos'
)

piechart.update_layout(showlegend=False)
#############################################################

v_bar = anvisa_df.groupby('Patrocinador do Estudo')['Número do Processo'].size().reset_index().sort_values(by='Número do Processo', ascending=False)
v_bar = v_bar.head(40)
vertical_bar = px.bar(
    v_bar,
    orientation='h',
    x='Número do Processo',
    y='Patrocinador do Estudo',
    color='Patrocinador do Estudo',
    title='Total por Patrocinador'
)

vertical_bar.update_layout(showlegend=False)

pie_drug = anvisa_df.groupby('Tipo de Medicamento Experimental')['Número do Processo'].size().reset_index().sort_values(by='Número do Processo', ascending=False)

pie_drug_chart = px.bar(
    pie_drug,
    orientation='h',
    x='Número do Processo',
    y='Tipo de Medicamento Experimental',
    color='Tipo de Medicamento Experimental',
    title='Total por Tipo de Medicamento Experimental'
)

pie_drug_chart.update_layout(showlegend=False)

bar_class = anvisa_df.groupby('Classe Terapêutica')['Número do Processo'].size().reset_index().sort_values(by='Número do Processo', ascending=False)
bar_class = bar_class.head(5)

bar_class_chart = px.bar(
    bar_class,
    orientation='h',
    x='Número do Processo',
    y='Classe Terapêutica',
    color='Classe Terapêutica',
    title='Total por Classe Terapêutica'
)

bar_class_chart.update_layout(showlegend=False)

pie_estudo = anvisa_df.groupby("Tipo de Estudo")["Número do Processo"].nunique().reset_index()

pie_estudo_chart = px.pie(
    pie_estudo,
    names="Tipo de Estudo",
    values="Número do Processo",
    title='% Tipo de Estudo'
)

pie_estudo_chart.update_layout(showlegend=False)

with col1:
    st.plotly_chart(piechart)
    st.plotly_chart(bar_class_chart)

with col2:
    st.plotly_chart(pie_drug_chart)
    st.plotly_chart(pie_estudo_chart)

# with col3:
#     st.plotly_chart(vertical_bar)

st.plotly_chart(vertical_bar)

st.dataframe(
    anvisa_df[['Patrocinador do Estudo', 'Nome ou Código do Medicamento Experimental', 'Tipo de Medicamento Experimental', 'Doença', 'Fase do Estudo', 'Situação do Estudo']],
    column_config= 
    {
        'Número do Processo': st.column_config.TextColumn()
    }
    )







# filtered_df = filter_dataframe(anvisa_df)

# # Proceed with your plotting and dataframe display using filtered_df
# # Example for plotting
# pie = filtered_df.groupby('Situação do Estudo')['Número do Processo'].nunique().reset_index()
# piechart = px.pie(pie, values='Número do Processo', names='Situação do Estudo', title='% da Situações dos Estudos')
# st.plotly_chart(piechart)