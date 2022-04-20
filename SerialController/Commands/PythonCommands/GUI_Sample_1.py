#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button
from Commands.PythonCommandBase import ImageProcPythonCommand
import tkinter as tk
from tkinter import ttk

from decimal import *


def round_half_down(x):  # 五捨五超入
    d = Decimal(x).quantize(Decimal("0"), rounding=ROUND_HALF_DOWN)
    return d


def round_half_up(x):  # 四捨五入
    d = Decimal(x).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    return d


# Modified版限定で動くかもしれない奴です
class GuiSample(ImageProcPythonCommand, tk.Frame):
    NAME = 'Guiのサンプル'

    def __init__(self, cam, master=None):
        super().__init__(cam, master)
        self.DynamaxCorrection = None
        self.DamageCorrection = None
        self.Yakedo = None
        self.TypeCompatibility = None
        self.TypeBuff = None
        self.random = None
        self.CriticalHit = None
        self.WeatherBuff = None
        self.WeatherWeak = None
        self.Oyakoai = None
        self.attack_multi = None
        self.DamageCalc = None
        self.Checkbox = None
        self.CheckboxVariable = None
        self.cam = cam
        self.preview = master.master.master
        self.SampleGui = None
        self.Targets = 1.0
        self.Weather = 1.0
        self.Badge = 1.0
        self.Critical = 1.0
        self.STAB = 1.0
        self.Type = 1.0
        self.isHarikiri = False
        self.AttackRank1 = 1.0
        self.AttackRank2 = 1.0
        self.DefenceRank1 = 1.0
        self.DefenceRank2 = 1.0

    def do(self):
        # self.SampleGui = tk.Toplevel(self.preview)
        self.SampleGui = tk.Toplevel()
        self.DamageCalc = DamageCalc(self.SampleGui)
        self.DamageCalc.pack()

        self.DamageCalc.Level.trace_add("write", self.update)
        self.DamageCalc.Level_2.trace_add("write", self.update)
        self.DamageCalc.Attack.trace_add("write", self.update)
        self.DamageCalc.Attack_2.trace_add("write", self.update)
        self.DamageCalc.SpAttack.trace_add("write", self.update)
        self.DamageCalc.SpAttack_2.trace_add("write", self.update)
        self.DamageCalc.Defence.trace_add("write", self.update)
        self.DamageCalc.Defence_2_2.trace_add("write", self.update)
        self.DamageCalc.SpDefence.trace_add("write", self.update)
        self.DamageCalc.SpDefence_2_2.trace_add("write", self.update)
        self.DamageCalc.Move.trace_add("write", self.update)
        self.DamageCalc.Move_2.trace_add("write", self.update)

    def update(self, *args):
        tekioryoku = False
        damage = 2 * self.DamageCalc.Level.get() // 5 + 2
        damage = damage * self.last_power() * self.last_attack() // self.last_defence()
        damage = int(damage // 50 + 2)
        if self.attack_multi:
            damage = round_half_up(damage * 3072 / 4096)
        if self.Oyakoai:
            damage_oyakoai = round_half_up(damage * 1024 / 4096)
        if self.WeatherWeak:
            damage = round_half_up(damage * 2048 / 4096)
        if self.WeatherBuff:
            damage = round_half_up(damage * 6144 / 4096)
        if self.CriticalHit:
            damage = round_half_up(damage * 6144 / 4096)
        if self.random:
            damage_min = int(damage * 0.85)
        if self.TypeBuff:
            if tekioryoku:
                damage = round_half_up(damage * 8192 / 4096)
            else:
                damage = round_half_up(damage * 6144 / 4096)
        if self.TypeCompatibility:
            damage = round_half_up(damage * 6144 / 4096)
        if self.Yakedo:
            damage = round_half_up(damage * 1024 / 4096)
        if self.DamageCorrection:
            damage = round_half_up(damage * 1024 / 4096)
        if self.DynamaxCorrection:
            damage = round_half_up(damage * 1024 / 4096)

        # 1
        multiplier = 1
        if multiplier != 1:
            power = round_half_up(4096 * multiplier / 4096)
        else:
            power = round_half_up(4096)
        power = round_half_down(self.DamageCalc.Move.get() * power / 4096)
        if power < 1:
            power = 1
        # /2
        # 3
        atk_rank = int(self.DamageCalc.Attack.get() * self.AttackRank1)
        if self.isHarikiri:
            atk_rank_ = atk_rank * 6144 // 4096
        else:
            atk_rank_ = atk_rank * 1

        multiplier = 1
        if multiplier != 1:
            atk = round_half_up(4096 * multiplier / 4096)
        else:
            atk = round_half_up(4096)
        atk_ = round_half_down(atk_rank_ * atk / 4096)
        if atk_ < 1:
            atk_ = 1
        # /4

        defence_rank = int(self.DamageCalc.Defence_2_2.get() * self.DefenceRank2)
        isSunaArashiAndIwaType = False
        if isSunaArashiAndIwaType:
            defence_rank_ = defence_rank * 6144 // 4096
        else:
            defence_rank_ = defence_rank * 1

        multiplier = 1
        if multiplier != 1:
            defe = round_half_up(4096 * multiplier / 4096)
        else:
            defe = round_half_up(4096)
        defe_ = round_half_down(defence_rank_ * defe / 4096)
        if defe_ < 1:
            defe_ = 1
        damage = (damage * power * atk_ // defe_) // 50 + 2

        self.DamageCalc.res_1to2.set(damage)
        # print(f"レベルは{value}です．")

    def last_power(self) -> int:
        m = 0
        return m

    def last_attack(self) -> int:
        m = 0
        return m

    def last_defence(self) -> int:
        m = 0
        return m


class DamageCalc(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(DamageCalc, self).__init__(master, **kw)
        self.labelframe_Pokemon_1 = ttk.Labelframe(self)
        self.label_level = ttk.Label(self.labelframe_Pokemon_1)
        self.label_level.configure(font='TkMenuFont', text='Lv')
        self.label_level.grid(row='0')
        self.label_HP = ttk.Label(self.labelframe_Pokemon_1)
        self.label_HP.configure(font='TkMenuFont', text='HP')
        self.label_HP.grid(row='1')
        self.label_Attack = ttk.Label(self.labelframe_Pokemon_1)
        self.label_Attack.configure(text='こうげき')
        self.label_Attack.grid(column='0', row='2')
        self.label_SpAttack = ttk.Label(self.labelframe_Pokemon_1)
        self.label_SpAttack.configure(text='とくこう')
        self.label_SpAttack.grid(column='0', row='3')
        self.label_Defence = ttk.Label(self.labelframe_Pokemon_1)
        self.label_Defence.configure(text='ぼうぎょ')
        self.label_Defence.grid(row='4')
        self.label_SpDefence = ttk.Label(self.labelframe_Pokemon_1)
        self.label_SpDefence.configure(text='とくぼう')
        self.label_SpDefence.grid(row='5')
        self.entry_level = ttk.Entry(self.labelframe_Pokemon_1)
        self.Level = tk.IntVar(value='')
        self.entry_level.configure(textvariable=self.Level)
        self.entry_level.grid(column='1', row='0')
        self.entry_HP = ttk.Entry(self.labelframe_Pokemon_1)
        self.HP = tk.IntVar(value='')
        self.entry_HP.configure(textvariable=self.HP)
        self.entry_HP.grid(column='1', row='1')
        self.entry_Attack = ttk.Entry(self.labelframe_Pokemon_1)
        self.Attack = tk.IntVar(value='')
        self.entry_Attack.configure(textvariable=self.Attack)
        self.entry_Attack.grid(column='1', row='2')
        self.entry_SpAttack = ttk.Entry(self.labelframe_Pokemon_1)
        self.SpAttack = tk.IntVar(value='')
        self.entry_SpAttack.configure(textvariable=self.SpAttack)
        self.entry_SpAttack.grid(column='1', row='3')
        self.entry_Defence = ttk.Entry(self.labelframe_Pokemon_1)
        self.Defence = tk.IntVar(value='')
        self.entry_Defence.configure(textvariable=self.Defence)
        self.entry_Defence.grid(column='1', row='4')
        self.entry_SpDefence = ttk.Entry(self.labelframe_Pokemon_1)
        self.SpDefence = tk.IntVar(value='')
        self.entry_SpDefence.configure(textvariable=self.SpDefence)
        self.entry_SpDefence.grid(column='1', row='5')
        self.label_move = ttk.Label(self.labelframe_Pokemon_1)
        self.label_move.configure(text='技威力')
        self.label_move.grid(row='6')
        self.entry_move = ttk.Entry(self.labelframe_Pokemon_1)
        self.Move = tk.IntVar(value='')
        self.entry_move.configure(textvariable=self.Move)
        self.entry_move.grid(column='1', row='6')
        self.labelframe_Pokemon_1.configure(height='200', padding='5', text='ポケモン1', width='200')
        self.labelframe_Pokemon_1.grid(column='0', ipadx='5', ipady='5', padx='5', pady='5', row='0')
        self.labelframe_pokemon_2 = ttk.Labelframe(self)
        self.label_level__2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_level__2.configure(font='TkMenuFont', text='Lv')
        self.label_level__2.grid(row='0')
        self.label_hp_2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_hp_2.configure(font='TkMenuFont', text='HP')
        self.label_hp_2.grid(row='1')
        self.label_attack_2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_attack_2.configure(text='こうげき')
        self.label_attack_2.grid(column='0', row='2')
        self.label_spattack_2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_spattack_2.configure(text='とくこう')
        self.label_spattack_2.grid(column='0', row='3')
        self.label_defence_2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_defence_2.configure(text='ぼうぎょ')
        self.label_defence_2.grid(row='4')
        self.label_spdefence_2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_spdefence_2.configure(text='とくぼう')
        self.label_spdefence_2.grid(row='5')
        self.entry_level_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.Level_2 = tk.IntVar(value='')
        self.entry_level_2.configure(textvariable=self.Level_2)
        self.entry_level_2.grid(column='1', row='0')
        self.entry_hp_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.HP_2 = tk.IntVar(value='')
        self.entry_hp_2.configure(textvariable=self.HP_2)
        self.entry_hp_2.grid(column='1', row='1')
        self.entry_attack_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.Attack_2 = tk.IntVar(value='')
        self.entry_attack_2.configure(textvariable=self.Attack_2)
        self.entry_attack_2.grid(column='1', row='2')
        self.entry_spattack_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.SpAttack_2 = tk.IntVar(value='')
        self.entry_spattack_2.configure(textvariable=self.SpAttack_2)
        self.entry_spattack_2.grid(column='1', row='3')
        self.entry_defence_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.Defence_2_2 = tk.IntVar(value='')
        self.entry_defence_2.configure(textvariable=self.Defence_2_2)
        self.entry_defence_2.grid(column='1', row='4')
        self.entry_spdefence_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.SpDefence_2_2 = tk.IntVar(value='')
        self.entry_spdefence_2.configure(state='normal', textvariable=self.SpDefence_2_2)
        self.entry_spdefence_2.grid(column='1', row='5')
        self.label_move_2 = ttk.Label(self.labelframe_pokemon_2)
        self.label_move_2.configure(text='技威力')
        self.label_move_2.grid(row='6')
        self.entry_move_2 = ttk.Entry(self.labelframe_pokemon_2)
        self.Move_2 = tk.IntVar(value='')
        self.entry_move_2.configure(textvariable=self.Move_2)
        self.entry_move_2.grid(column='1', row='6')
        self.labelframe_pokemon_2.configure(height='200', padding='5', text='ポケモン2', width='200')
        self.labelframe_pokemon_2.grid(column='1', ipadx='5', ipady='5', padx='5', pady='5', row='0')
        self.labelframe_Result = ttk.Labelframe(self)
        self.label_1to2 = ttk.Label(self.labelframe_Result)
        self.label_1to2.configure(text='ポケモン1　→　ポケモン2')
        self.label_1to2.grid(padx='5')
        self.label_2to1 = ttk.Label(self.labelframe_Result)
        self.label_2to1.configure(text='ポケモン2　→　ポケモン1')
        self.label_2to1.grid(padx='5', row='1')
        self.entry_13 = ttk.Entry(self.labelframe_Result)
        self.res_1to2 = tk.IntVar(value='')
        self.entry_13.configure(textvariable=self.res_1to2)
        self.entry_13.grid(column='1', padx='5', row='0')
        self.entry_14 = ttk.Entry(self.labelframe_Result)
        self.res_2to1 = tk.IntVar(value='')
        self.entry_14.configure(textvariable=self.res_2to1)
        self.entry_14.grid(column='1', padx='5', row='1')
        self.labelframe_Result.configure(height='200', text='計算結果', width='200')
        self.labelframe_Result.grid(column='0', columnspan='2', ipadx='5', ipady='5', padx='5', pady='5', row='1',
                                    rowspan='1', sticky='ew')
        self.configure(height='200', width='200')
        self.grid()
        self.rowconfigure('1', uniform='None')
        self.columnconfigure('0', uniform='None')


if __name__ == '__main__':
    root = tk.Tk()
    widget = DamageCalc(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()
