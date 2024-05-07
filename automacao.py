# Programa para automatizar cadastro de produtos

import pyautogui as pg
import pandas as pd
import time

pg.PAUSE = 0.5

pg.press('win') 
pg.write('opera')
pg.press('enter')
pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pg.press('enter')
time.sleep(3)
pg.press('tab')
pg.write('daniel.python@hotmail.com')
pg.press('tab')
pg.write('jornadapython')
pg.press('tab')
pg.press('enter')
time.sleep(2)
df_produtos = pd.read_csv('produtos.csv')


for linha in df_produtos.index:   
    pg.click(x=554, y=222)
    pg.write(str(df_produtos.loc[linha, 'codigo']))
    pg.press('tab')
    pg.write(str(df_produtos.loc[linha, 'marca']))
    pg.press('tab')
    pg.write(str(df_produtos.loc[linha, 'tipo']))
    pg.press('tab')
    pg.write(str(df_produtos.loc[linha, 'categoria']))
    pg.press('tab')
    pg.write(str(df_produtos.loc[linha, 'preco_unitario']))
    pg.press('tab')
    pg.write(str(df_produtos.loc[linha, 'custo']))
    pg.press('tab')
    obs = df_produtos.loc[linha, 'obs']
    if not pd.isna(obs):
        pg.write(str(df_produtos.loc[linha, 'obs']))
    pg.press('tab')
    pg.press('enter')
    pg.press('home')