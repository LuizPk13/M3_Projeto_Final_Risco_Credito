"""
Engenharia de atributos.
A mesma função é usada no treino (notebook) e na API, garantindo o mesmo cálculo.
"""

import numpy as np
import pandas as pd


def adicionar_comprometimento_renda(df: pd.DataFrame) -> pd.DataFrame:
    """Cria comprometimento_renda = (loan_amnt / person_income) * 100.

    Indica quantos % da renda anual o empréstimo representa.
    """
    df = df.copy()  # não altera o DataFrame original

    # Proteção contra divisão por zero: renda 0 vira nulo (tratado depois pelo pipeline)
    renda = df["person_income"].replace(0, np.nan)

    df["comprometimento_renda"] = (df["loan_amnt"] / renda) * 100
    return df
