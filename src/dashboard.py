import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import locale

# flake8: noqa


def format_moeda(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor, grouping=True, symbol=None)
    return valor


st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Fluxo de caixa TecnoJR em 2023</h1><br>", unsafe_allow_html=True)

df = pd.read_excel('./data/livro_caixa.xlsx')

total_entradas = df[df['Fluxo de caixa'] == 'Entrada']['Valor'].sum()
total_saidas = df[df['Fluxo de caixa'] == 'Saída']['Valor'].sum()
saldo_anterior = 1702.32
caixa = total_entradas - total_saidas + saldo_anterior
conta_pagar_mes = 600 + 217.42 + 126.50
conta_pagar_futuras = 3800 + 1000 + 600 + 126.50
conta_receber_mes = 1875.0 + 425 * 2
conta_receber_futuras = 1875.0 + 850 + 15000

#col1, col2, col3 = st.columns(3)
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total de receita bruta em 2023", f"R$ {format_moeda(total_entradas)}",
            delta=f"R$ {format_moeda(total_entradas - 0)}")
col2.metric("Total de despesas em 2023", f"R$ {format_moeda(total_saidas)}",
            delta=f"-R$ {format_moeda(total_saidas)}")
col3.metric("Saldo Atual", f"R$ {format_moeda(caixa)}",
            delta=f"R$ {format_moeda(caixa + conta_receber_mes + conta_receber_futuras - conta_pagar_mes - conta_pagar_futuras)}")
col4.metric("Total de contas a receber em novembro", f"R$ {format_moeda(conta_receber_mes)}",
            delta=f"R$ {format_moeda(conta_receber_futuras)}")
col5.metric("Total de contas a pagar em novembro", f"R$ {format_moeda(conta_pagar_mes)}",
            delta=f"-R$ {format_moeda(conta_pagar_futuras)}")


# Fluxo de caixa por mês
df_grouped_by_month = df.groupby([df['Data'].dt.month, 'Fluxo de caixa']).agg({'Valor': 'sum'}).reset_index()
df_grouped_by_month['Valor'] = df_grouped_by_month['Valor'].apply(lambda x: round(x, 2))

novas_linhas = [{'Data': 1, 'Fluxo de caixa': 'Entrada', 'Valor': 0},
                {'Data': 5, 'Fluxo de caixa': 'Entrada', 'Valor': 0}]
novo_df = pd.DataFrame(novas_linhas)

df_grouped_by_month = pd.concat([df_grouped_by_month, novo_df],
                                ignore_index=True).sort_values(by=['Data', 'Fluxo de caixa']).reset_index(drop=True)

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

st.markdown("<br>", unsafe_allow_html=True)

df_grouped_by_month['Data'] = df_grouped_by_month['Data'].apply(lambda x: meses[x])

# Inverte a ordem das cores
color_discrete_sequence = ['#00CC96', '#EF553B']

fig = px.bar(df_grouped_by_month, x='Data', y='Valor', color='Fluxo de caixa', barmode='group',
            text_auto='.2s', color_discrete_sequence=color_discrete_sequence,
            title='Total de receita bruta e despesas por mês')

fig.update_xaxes(title_text="Mês")
fig.update_yaxes(title_text="Valor (R$)")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.update_layout(
    title_x=0.2,  # Centraliza o título horizontalmente
    title_font=dict(size=32)  # Define o tamanho da fonte do título
)
st.plotly_chart(fig, use_container_width=True)


# Tabela com a receita bruta e despesas do mês selecionado
selected_month = st.sidebar.selectbox("Mês", df_grouped_by_month['Data'].unique())
df_select_month = df[df['Data'].dt.month == list(meses.keys())[list(meses.values()).index(selected_month)]]

df_selected_month = df[df['Data'].dt.month == list(meses.keys())[list(meses.values()).index(selected_month)]]
df_selected_month.loc[::, 'Data'] = df_selected_month['Data'].dt.day
df_selected_month.loc[::, 'Valor'] = df_selected_month['Valor'].apply(lambda x: f"R$ {format_moeda(x)}")

selected_columns = ['Dia', 'Nome', 'Descrição', 'Classificação', 'Valor', 'Fluxo de caixa']

texto_cor = 'white'
fundo_cor = 'rgba(0, 0, 0, 0)'
borda_cor = 'white'

st.markdown(f"<h2 style='text-align: center;'>Receitas e despesas em {selected_month} de 2023 </h2><br>", unsafe_allow_html=True)
fig = go.Figure(data=[go.Table(
    header=dict(values=selected_columns,
                fill_color=fundo_cor,
                align='left',
                font=dict(color=texto_cor, size=15)),
    cells=dict(values=[df_selected_month['Data'], df_selected_month['Nome'],
                    df_selected_month['Descrição'], df_selected_month['Classificação'],
                    df_selected_month['Valor'], df_selected_month['Fluxo de caixa']],
                fill_color=fundo_cor, 
                align='left'),
    columnwidth=[15, 80, 150, 45, 40, 40],),
])

fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(color=texto_cor, size=14),
    height=800,
)

st.plotly_chart(fig, use_container_width=True)