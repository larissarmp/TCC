tarifa_fatura = pd.read_sql_table('sideufg_fatura',engine)

columns = ['vencimento', 'data_leitura_anterior', 'data_leitura_atual',
           'demanda_contratada_ponta','demanda_contratada_geral', 'demanda_contratada_fora_ponta',
           'mes_referencia', 'valor']
tarifa_fatura.drop(columns, inplace=True, axis=1)

tarifa_fatura
tarifa_fatura.to_sql('dim_tarifa_fatura', con=engine, if_exists= 'append' )

