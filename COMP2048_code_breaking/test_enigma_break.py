# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time
import math

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
# print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring =""
print(crib_substring)

##Break the code via brute force search
#INSERT CODE HERE

# find all the possible combination of the key
start_time = time.time()
count = 0
for i in capitalLetters:
    for j in capitalLetters:
        for k in capitalLetters:
            key = i+j+k
            engine4 = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                   rotor.ROTOR_II, rotor.ROTOR_III, key= key,
                                   plugs="AA BB CC DD EE")
            decrypt = engine4.encipher(ShakesHorribleMessage)
            count += 1

            #Print the Decoded message
            if (decrypt[-12:] == crib):
                print("key is ", key)
                print("Decoded Message: ", decrypt)
                print("Number of tries: ", count)
                end_time = time.time()
                time_taken = end_time - start_time
                print("time taken: ", time_taken,'s')

rotor = 5*4*3
starting = 26**3
plugborad = math.factorial(26)/(math.factorial(10) * (math.factorial(6) * 2**10))
estimated_number = rotor*starting*plugborad
print(estimated_number)
#estimated_time = (time_taken*estimated_number)/count
#print("estimated time is ", estimated_time)
