import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__ )

@app.route('/')
def p_primos():
    primos = []
    for div in range(1,550+1):
        cont = 0

        for x in range(1,div+1):
            if div % x == 0:
                cont +=1
        
        if cont == 2:
            primos.append(x)

    primos1 = ''
    a = 0
    b = 10
    for j in range(1,10+1):
        for i in range(a,b):
            primos1 += str(primos[i]) + ',' 
        primos1 += ' --> ' + str(b) + '<br>'
        a += 10
        b += 10    

                    
    return primos1



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

