
#extrair dados para a tabela calendario
dfMedicao = pd.read_sql_table('sideufg_medicao',engine)
dfMedicao['year'] = pd.DatetimeIndex(dfMedicao['data_medicao']).year
dfMedicao['month'] = pd.DatetimeIndex(dfMedicao['data_medicao']).month
dfMedicao['day'] = pd.DatetimeIndex(dfMedicao['data_medicao']).day

dfMedicao['week'] = pd.DatetimeIndex(dfMedicao['data_medicao']).week
dfMedicao['day_name'] = pd.DatetimeIndex(dfMedicao['data_medicao']).day_name()
newdfMedicao = pd.DataFrame()
newdfMedicao = dfMedicao[dfMedicao.columns[4:11]]
newMedicao.to_sql('dim_dat_medicao', con=engine, if_exists= 'append' )
# -------------------------------------------------
