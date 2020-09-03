import os
import torch
import pandas as pd

def load_checkpoint(G, D, E, CD, fname):
    # load the highest savepoints of all models
    iteration = 0
    checkpoint_pth = './checkpoint/'
    if os.path.exists(checkpoint_pth):
        files = set(os.listdir(checkpoint_pth))
        highest_pth = 0 
        for s in files:
            curr_num = int(s.split('iter')[1].split('.')[0])
            highest_pth = max(highest_pth, curr_num)
        if files:
            D.load_state_dict(torch.load(f'./checkpoint/D{fname}{highest_pth}.pth'))
            CD.load_state_dict(torch.load(f'./checkpoint/CD{fname}{highest_pth}.pth'))
            E.load_state_dict(torch.load(f'./checkpoint/E{fname}{highest_pth}.pth'))
            G.load_state_dict(torch.load(f'./checkpoint/G{fname}{highest_pth}.pth'))
            iteration = highest_pth
    else:
        os.mkdir(checkpoint_pth)
    
    return iteration

def load_loss():
    if os.path.exists('./checkpoint/loss.csv'):
        return pd.read_csv('./checkpoint/loss.csv')
    else:
        return pd.DataFrame()
    
def add_loss(df, l, index):
    df = df.append(pd.DataFrame({
        'index': index,
        'loss:': l,
    }))
    
def write_loss(df):
    df.to_csv('./checkpoint/loss.csv')
    
