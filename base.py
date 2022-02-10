import basedosdados as bd 

query = """
        DESCRIBE basedosdados.br_ms_vacinacao_covid19.microdados_vacinacao
        
        """
df = bd.read_sql(query)