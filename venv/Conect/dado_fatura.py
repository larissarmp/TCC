dado_fatura = pd.read_sql_table('sideufg_dado_fatura',engine)
columns = ['consumo_atual','consumo_anterior','consumo_constante','demanda_atual',
           'demanda_atual','demanda_anterior','demanda_constante','reativo_atual',
           'ufer_anterior','ufer_constante','ufer_atual', 'dmcr_atual', 'dmcr_anterior',
           'dmcr_constante','demanda_ultr_atual','demanda_ultr_anterior','demanda_ultr_constante',
           'fator_potencia_atual','fator_potencia_anterior','fator_potencia_constante']
dado_fatura.drop(columns, inplace=True, axis=1)
dado_fatura
dado_fatura.to_sql('dim_dado_fatura', con=engine, if_exists= 'append' )