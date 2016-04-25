Skip to content
 
 
Search…
All gists
GitHub
New gist @jmcuestasb
  Star 0
  Fork 0
  @jormvngandrjormvngandr/PracticaIPython.ipynb
Created 21 hours ago
Embed  
<script src="https://gist.github.com/jormvngandr/fcc7486ccd26fa11b9bcad643e7e874f.js"></script>
  Download ZIP
 Code  Revisions 1
Unified Split
Revisions
 @jormvngandr jormvngandr created this gist 21 hours ago.
View 618  PracticaIPython.ipynb
@@ -0,0 1,618 @@
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Practica IPython : Analisis de insertion sort y merge sort\n",
    "\n",
    "<ol>\n",
    "<li>Analisis experimental de Insertion sort: <br>\n",
    "Correr insertion sort para arreglos de tamaño n = 4, 5, 6 y encuentre los coeficientes del polinomio cuadrático de la forma $An^{2}  Bn  C $ para el mejor caso, el peor caso y el caso promedio (este se debe calcular corriendo todas las permutaciones de tamaño n). Para encontrar el polinomio deben realizar la interpolación de los puntos de sus experimentos. En este punto deben graficar el polinomio encontrado. \n",
    "<br>\n",
    "\n",
    "<li>Análisis de Insertion sort  merge sort (Problem 1-2 CLRS del cormen): <br>\n",
    "El merge sort corre en tiempo Θ(n lg n) en el peor caso y insertion sort corre en Θ(n^2) en el peor caso. La constante en insertion sort hace que este algoritmo sea más rápido para valores de n suficientemente pequeños. Su tarea consiste en encontrar el valor k donde insertion sort empieza a ser menos eficiente que merge sort en el peor, mejor y caso promedio. Para este punto deben graficar lo siguiente:\n",
    "<ul type circle>\n",
    "<li> Experimento con insetion sort\n",
    "<li> Experimento con Merge sort\n",
    "<li> Experimento combinando Insertion sort con Merge sort\n",
    "</ul>\n",
    "<br>\n",
    "La gráfica se debe hacer con respecto a los datos del caso promedio\n",
    "</ol>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Punto 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Punto 1\n",
    "from random import randint\n",
    "import itertools\n",
    "import time\n",
    "import random\n",
    "import gc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def insertionSort(A):\n",
    "    j = 2\n",
    "    for j in xrange(len(A)):\n",
    "        key = A[j]\n",
    "        i = j - 1\n",
    "        while i >= 0 and A[i] > key:\n",
    "            A[i1] = A[i]\n",
    "            i = i - 1\n",
    "        A[i1] = key\n",
    "        \n",
    "def merge(A, p, q, r):\n",
    "    L = A[p:q1][float('inf')]\n",
    "    R = A[q1:r1][float('inf')]\n",
    "    i = 0\n",
    "    j = 0\n",
    "    for k in range(p, r  1):\n",
    "        if L[i] <= R[j]:\n",
    "            A[k] = L[i]\n",
    "            i = 1\n",
    "        else:\n",
    "            A[k] = R[j]\n",
    "            j = 1\n",
    "\n",
    "def mergeSortMain(A, p, r):\n",
    "    if p < r:\n",
    "        q = int((p  r) / 2.0)\n",
    "        mergeSortMain(A, p, q)\n",
    "        mergeSortMain(A, q  1, r)\n",
    "        merge(A, p, q, r)\n",
    "\n",
    "def mergeSort(A):\n",
    "    mergeSortMain(A, 0, len(A) - 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def randList(n):\n",
    "    A = [randint(1,n) for x in xrange(n)]\n",
    "    return A\n",
    "\n",
    "def arrAverage(A):\n",
    "    avg = 0\n",
    "    for i in A:\n",
    "        avg = avg  i\n",
    "    return avg / len(A)\n",
    "\n",
    "def arrPerm(A):\n",
    "    arrPermutations = []\n",
    "    for i in A:\n",
    "        arrTemp = []\n",
    "        for j in i:\n",
    "            arrTemp.append(j)\n",
    "        arrPermutations.append(arrTemp)\n",
    "    return arrPermutations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def averageCase(A):\n",
    "    averageTimes = []\n",
    "    perm = [x for x in itertools.permutations(A)]\n",
    "    for j in xrange(10):\n",
    "        for i in arrPerm(perm):\n",
    "            t1 = time.clock()\n",
    "            insertionSort(i)\n",
    "            t2 = time.clock() - t1\n",
    "            timeArr.append(t2)\n",
    "    return arrAverage(averageTimes)\n",
    "\n",
    "def bestCase(A):\n",
    "    bestTimes = []\n",
    "    for i in xrange(10):\n",
    "        A.sort()\n",
    "        t1 = time.clock()\n",
    "        insertionSort(A)\n",
    "        t2 = time.clock() - t1\n",
    "        bestTimes.append(t2)\n",
    "    return arrAverage(bestTimes)\n",
    "\n",
    "def worstCase(A):\n",
    "    worstTimes = []\n",
    "    for i in xrange(10):\n",
    "        A.sort()\n",
    "        A.reverse()\n",
    "        t1 = time.clock()\n",
    "        insertionSort(A)\n",
    "        t2 = time.clock() - t1\n",
    "        worstTimes.append(t2)\n",
    "    return arrAverage(worstTimes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def testBWA(n):\n",
    "    best = []\n",
    "    worst = []\n",
    "    average = []\n",
    "    for x in xrange(10):\n",
    "        A = randList(n)\n",
    "        best.append(bestCase(A))\n",
    "        worst.append(worstCase(A))\n",
    "        average.append(averageCase(A))\n",
    "    return arrAverage(best) , arrAverage(worst) , arrAverage(average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "n =  4  Best case =  1.32243645794e-06  Worst case =  2.12379347204e-06  Average case =  1.65403246432e-06\n",
      "n =  5  Best case =  1.88299160527e-06  Worst case =  3.17384749337e-06  Average case =  2.60144962786e-06\n",
      "n =  6  Best case =  2.40012348286e-06  Worst case =  4.35417137396e-06  Average case =  2.72017284051e-06\n"
     ]
    }
   ],
   "source": [
    "for case in xrange(4,7):\n",
    "    a = testBWA(case)\n",
    "    print \"n = \", case,\" Best case = \",a[0],\" Worst case = \", a[1],\" Average case = \", a[2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Tomaremos los anteriores datos para realizar la interpolación, pues, los datos varian cada vez que se ejecuta el programa. <br>\n",
    "<br>\n",
    "Despues de interpolar se tienen los siguientes polinomios : <br>\n",
    "Mejor caso : $2.17116x10^{-8}n^{2}  3.65151x10^{-7}n - 4.85588x10^{-7}$  <br>\n",
    "Peor caso : $6.51349x10^{-8}n^{2}  4.63836x10^{-7}n - 7.77502x10^{-7}$ <br>\n",
    "Caso promedio : $4.14347x10^{-8}n^{2}  5.74505x10^{-7}n - 1.31097x10^{-6}$ <br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Grafica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7789d68>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nVZ01a5befPPNGhERcURahw4dCsosW7ZMzzrrLG3QoIH26NHjiNASERERuSTT2rv3r21Tp06umPH\nDp0yZYq2bdtW69evr23bttXPPvtMN23apLVr19bq1atrvXr1NDg4uEj5WrVqpa99lqx8u/YsUPP\nPfdcbdiwoTZq1Eivv/563b9/f8H1l156SZs3b67169fXTp06FYTVyMvL0xdffFHbtWunoaGhet11\n1mffvK35El4KvP3mLJZ88e1XbtVF9/3T0ZOM6Rkus//r56JtSUlUdMGCATpw4UVVV7733Xp0y\nZYo9dRTR6TdeuutqqqakpKiwcHBumnn2pubq5Onz5dg4ODNSUlRVWNUgoPD9dNmzZpbm6u7t/\nXwMDA3Xbtm2qqhoXF6cbN25UVTN917dv32Ll2rx5swYEBOiuXbuKzbN93ZduHChZmdna1JSkvbv\n318ffPBBVVXdsmWLtmzZUuPi4lTVxGfauXOnqqpOnDhRe/XqpTExMXr48GG98847ddiwYeXuw5Lw\n5WdvscTEqHbooPrKK7KcbxKyU7fVTBuRkPv378/ixcvBmDJkiX07duXPn36HJHWv39/wMRPOvnk\nkxkfDgBAQEMHTqUTp068dVXXxXUN3LkSDp16kRAQEBBfKU///yTrKwswsLCOOWUU8okV35025JC\nprdr147zzjuP6tWr07BhQx588EFeUXAKpVq8bhw4f566/yMnJoVWrVrRp0waA9957jeff56m\nTZtSo0YNnnnmGT7//HPy8vKOsfcsFv8lPh7OPRduvhkeecRtaY4Pq5QqGHUxGnq/fv1YunQp/bt\nIykpiXbt2nHOOeewfPly9u3bx19//VWwnhQTE0N4ePgR5cPDwwuC7QG09PDUWKdOHWbOnMn//vc/\nmjZtyuDBg9myZUuZ5GrYsCFAiSHTExISGDZsGC1atKBBgwbccMMNBeHS27Vrx8SJExkzZgxhYWEM\nHz68ICR6VFQUV1xxRUHI9M6dO1OjRg3i4PLJJvF4u8kJJg1pGHDYPRot6U5fqxSqkL06tWL1NRU\nJk2aRG9n23b9vVp1qwZkyZNonnz5gWKqFmzZuzateuI8rt376Z5838PBU2XrjgggtYsGABcXFx\ndOzYkdtvv73IfIXp2LEjLVu2ZM6cOcXmeeKJJwgICGDDhg2kpqbyySef5EjAjB06FCWLFlCVFQU\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x72ef6a0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import math\n",
    "import numpy as np\n",
    "import pylab as pl\n",
    "%matplotlib inline\n",
    "pl.clf()\n",
    "sizes = np.arange(1,100,1)\n",
    "pl.plot(sizes, 2.17116e-08*sizes**2  3.65151e-07*sizes -4.85588e-07, 'r-', label = \"Best Case\")\n",
    "pl.plot(sizes, 6.51349e-08*sizes**2  4.63836e-07*sizes -7.77502e-07, 'b', label = \"Worst Case\")\n",
    "pl.plot(sizes, 4.14347e-08*sizes**2  5.74505e-07*sizes -1.31097e-06, 'y', label = \"Average Case\")\n",
    "pl.xlabel('X')\n",
    "pl.ylabel('Seconds')\n",
    "pl.title('Grafico de los polinomios de Insertion Sort')\n",
    "pl.legend(loc = 'upper left')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Punto 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def insertionCase(A):\n",
    "    insertionTimes = []\n",
    "    gc.collect()\n",
    "    for i in xrange(10):\n",
    "        B = list(A)\n",
    "        t1 = time.clock()\n",
    "        insertionSort(B)\n",
    "        t2 = time.clock() - t1\n",
    "        insertionTimes.append(t2)\n",
    "    return arrAverage(insertionTimes)\n",
    "\n",
    "def mergeCase(A):\n",
    "    mergeTimes = []\n",
    "    gc.collect()\n",
    "    for i in xrange(10):\n",
    "        B = list(A)\n",
    "        t1 = time.clock()\n",
    "        mergeSort(B)\n",
    "        t2 = time.clock() - t1\n",
    "        mergeTimes.append(t2)\n",
    "    return arrAverage(mergeTimes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def averageCase2(n):\n",
    "    mergeTimes = []\n",
    "    insertionTimes = []\n",
    "    for i in xrange(10):\n",
    "        A = randList(n)\n",
    "        random.shuffle(A)\n",
    "        mergeTimes.append(mergeCase(A))\n",
    "        insertionTimes.append(insertionCase(A))\n",
    "    return \"Merge: \",arrAverage(mergeTimes),\" Insertion: \",arrAverage(insertionTimes)\n",
    "\n",
    "def bestCase2(n):\n",
    "    mergeTimes = []\n",
    "    insertionTimes = []\n",
    "    for i in xrange(10):\n",
    "        A = randList(n)\n",
    "        A.sort()\n",
    "        mergeTimes.append(mergeCase(A))\n",
    "        insertionTimes.append(insertionCase(A))\n",
    "    return \"Merge: \",arrAverage(mergeTimes),\" Insertion: \",arrAverage(insertionTimes)\n",
    "\n",
    "def worstCase2(n):\n",
    "    mergeTimes = []\n",
    "    insertionTimes = []\n",
    "    for i in xrange(10):\n",
    "        A = randList(n)\n",
    "        A.sort()\n",
    "        A.reverse()\n",
    "        mergeTimes.append(mergeCase(A))\n",
    "        insertionTimes.append(insertionCase(A))\n",
    "    return \"Merge: \",arrAverage(mergeTimes),\" Insertion: \",arrAverage(insertionTimes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Case : n =  10 , Times =  ('Merge: ', 4.340354879218466e-05, ' Insertion: ', 8.080678881015045e-06)\n",
      "Best Case : n =  10 , Times =  ('Merge: ', 3.482942345954143e-05, ' Insertion: ', 3.0198922070212574e-06)\n",
      "Worst Case : n =  10 , Times =  ('Merge: ', 3.258720285430172e-05, ' Insertion: ', 7.816191598521983e-06)\n",
      "Average Case : n =  20 , Times =  ('Merge: ', 7.307744385570912e-05, ' Insertion: ', 1.5198150326796166e-05)\n",
      "Best Case : n =  20 , Times =  ('Merge: ', 9.204157740100526e-05, ' Insertion: ', 5.238427410176882e-06)\n",
      "Worst Case : n =  20 , Times =  ('Merge: ', 7.444330360272033e-05, ' Insertion: ', 2.8454095466941e-05)\n",
      "Average Case : n =  30 , Times =  ('Merge: ', 0.0001428310324968152, ' Insertion: ', 3.208980883186996e-05)\n",
      "Best Case : n =  30 , Times =  ('Merge: ', 0.00013108700722796129, ' Insertion: ', 6.0674174267205676e-06)\n",
      "Worst Case : n =  30 , Times =  ('Merge: ', 0.00011078859452254618, ' Insertion: ', 5.785955567603196e-05)\n",
      "Average Case : n =  40 , Times =  ('Merge: ', 0.00014959717006718165, ' Insertion: ', 6.111630216992126e-05)\n",
      "Best Case : n =  40 , Times =  ('Merge: ', 0.00018211726419053775, ' Insertion: ', 7.449067433071831e-06)\n",
      "Worst Case : n =  40 , Times =  ('Merge: ', 0.00015204071683228904, ' Insertion: ', 0.00010927272705885116)\n",
      "Average Case : n =  50 , Times =  ('Merge: ', 0.00020225382647709008, ' Insertion: ', 8.083836944138056e-05)\n",
      "Best Case : n =  50 , Times =  ('Merge: ', 0.00022288778277811615, ' Insertion: ', 9.351796912824283e-06)\n",
      "Worst Case : n =  50 , Times =  ('Merge: ', 0.00018734779644660193, ' Insertion: ', 0.00016339393249609205)\n",
      "Average Case : n =  60 , Times =  ('Merge: ', 0.00026121475460058716, ' Insertion: ', 0.0001258446322776763)\n",
      "Best Case : n =  60 , Times =  ('Merge: ', 0.00023510156903512326, ' Insertion: ', 1.1594017539664492e-05)\n",
      "Worst Case : n =  60 , Times =  ('Merge: ', 0.0002212534881755346, ' Insertion: ', 0.00024328093721123875)\n",
      "Average Case : n =  70 , Times =  ('Merge: ', 0.00026869145505315823, ' Insertion: ', 0.0001651584969636133)\n",
      "Best Case : n =  70 , Times =  ('Merge: ', 0.00027301404584704873, ' Insertion: ', 1.266380941274292e-05)\n",
      "Worst Case : n =  70 , Times =  ('Merge: ', 0.0002774037453752953, ' Insertion: ', 0.000334884334176877)\n",
      "Average Case : n =  80 , Times =  ('Merge: ', 0.00029371116329798494, ' Insertion: ', 0.0002000984524306659)\n",
      "Best Case : n =  80 , Times =  ('Merge: ', 0.00032482197438980624, ' Insertion: ', 1.3398057716358381e-05)\n",
      "Worst Case : n =  80 , Times =  ('Merge: ', 0.00030441302967574305, ' Insertion: ', 0.0004012351161748029)\n",
      "Average Case : n =  90 , Times =  ('Merge: ', 0.0003659240889862758, ' Insertion: ', 0.0002625214007730392)\n",
      "Best Case : n =  90 , Times =  ('Merge: ', 0.00034213207548305035, ' Insertion: ', 1.528499689015916e-05)\n",
      "Worst Case : n =  90 , Times =  ('Merge: ', 0.0003661017297042691, ' Insertion: ', 0.0005164134102119533)\n",
      "Average Case : n =  100 , Times =  ('Merge: ', 0.0003892621317652356, ' Insertion: ', 0.00031343717815275336)\n",
      "Best Case : n =  100 , Times =  ('Merge: ', 0.00040534848568768217, ' Insertion: ', 1.7491689369535383e-05)\n",
      "Worst Case : n =  100 , Times =  ('Merge: ', 0.0006741860008878576, ' Insertion: ', 0.0009895732793654586)\n",
      "Average Case : n =  110 , Times =  ('Merge: ', 0.0006555100400566971, ' Insertion: ', 0.0005896211239235072)\n",
      "Best Case : n =  110 , Times =  ('Merge: ', 0.0006138118421654325, ' Insertion: ', 2.7573787019719016e-05)\n",
      "Worst Case : n =  110 , Times =  ('Merge: ', 0.0006088536923425636, ' Insertion: ', 0.0009720539569900667)\n",
      "Average Case : n =  120 , Times =  ('Merge: ', 0.0006093747717841324, ' Insertion: ', 0.0006641275886727271)\n",
      "Best Case : n =  120 , Times =  ('Merge: ', 0.00048338013179204613, ' Insertion: ', 2.8335668314412033e-05)\n",
      "Worst Case : n =  120 , Times =  ('Merge: ', 0.0006161922277794929, ' Insertion: ', 0.001122732761643874)\n",
      "Average Case : n =  130 , Times =  ('Merge: ', 0.0004991546275527981, ' Insertion: ', 0.0005733413390032638)\n",
      "Best Case : n =  130 , Times =  ('Merge: ', 0.0005317339352632189, ' Insertion: ', 2.9160710762425876e-05)\n",
      "Worst Case : n =  130 , Times =  ('Merge: ', 0.0005085498477615147, ' Insertion: ', 0.0010643165983969993)\n",
      "Average Case : n =  140 , Times =  ('Merge: ', 0.000534663033323568, ' Insertion: ', 0.0006415672174705378)\n",
      "Best Case : n =  140 , Times =  ('Merge: ', 0.0005377184536780532, ' Insertion: ', 2.4968389818695873e-05)\n",
      "Worst Case : n =  140 , Times =  ('Merge: ', 0.0005453609521248382, ' Insertion: ', 0.0012564725369406914)\n",
      "Average Case : n =  150 , Times =  ('Merge: ', 0.0005719478462640382, ' Insertion: ', 0.0007672342090165785)\n",
      "Best Case : n =  150 , Times =  ('Merge: ', 0.0005914133213934748, ' Insertion: ', 4.432728052051971e-05)\n",
      "Worst Case : n =  150 , Times =  ('Merge: ', 0.0005786626654082738, ' Insertion: ', 0.0014390161388553224)\n",
      "Average Case : n =  160 , Times =  ('Merge: ', 0.0006137289431637782, ' Insertion: ', 0.0008444842359597259)\n",
      "Best Case : n =  160 , Times =  ('Merge: ', 0.0006684225464732663, ' Insertion: ', 2.682769599573476e-05)\n",
      "Worst Case : n =  160 , Times =  ('Merge: ', 0.0006336207560173079, ' Insertion: ', 0.0016441359022542202)\n",
      "Average Case : n =  170 , Times =  ('Merge: ', 0.0006648736796842058, ' Insertion: ', 0.0009293491283563071)\n",
      "Best Case : n =  170 , Times =  ('Merge: ', 0.0006807468647411953, ' Insertion: ', 2.9125182621783093e-05)\n",
      "Worst Case : n =  170 , Times =  ('Merge: ', 0.0007397196355702817, ' Insertion: ', 0.0018438435451093936)\n",
      "Average Case : n =  180 , Times =  ('Merge: ', 0.0007178461418220649, ' Insertion: ', 0.0010727999295818337)\n",
      "Best Case : n =  180 , Times =  ('Merge: ', 0.0007195791257186102, ' Insertion: ', 3.364515199905327e-05)\n",
      "Worst Case : n =  180 , Times =  ('Merge: ', 0.0007064534504343102, ' Insertion: ', 0.0020483988057821987)\n",
      "Average Case : n =  190 , Times =  ('Merge: ', 0.0007946895688951373, ' Insertion: ', 0.001218106089405637)\n",
      "Best Case : n =  190 , Times =  ('Merge: ', 0.0007914367699720512, ' Insertion: ', 3.0846323807054435e-05)\n",
      "Worst Case : n =  190 , Times =  ('Merge: ', 0.0007826297379256175, ' Insertion: ', 0.002286401839880909)\n",
      "Average Case : n =  200 , Times =  ('Merge: ', 0.0008089679350575807, ' Insertion: ', 0.001294298167180159)\n",
      "Best Case : n =  200 , Times =  ('Merge: ', 0.000831358560683384, ' Insertion: ', 3.1975329249007694e-05)\n",
      "Worst Case : n =  200 , Times =  ('Merge: ', 0.00083689305594703, ' Insertion: ', 0.002531723671575037)\n"
     ]
    }
   ],
   "source": [
    "casos = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]\n",
    "for i in casos:\n",
    "    print \"Average Case : n = \",i,\", Times = \", averageCase2(i)\n",
    "    print \"Best Case : n = \",i,\", Times = \", bestCase2(i)\n",
    "    print \"Worst Case : n = \",i,\", Times = \", worstCase2(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hallar K"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Según los resultados anteriores, se puede ver como nunca merge es mejor que insertion si se compara sobre el mejor caso de insertion, para el peor caso se observa como desde n = 70 merge tiende a ser mejor que insertion, y para el caso promedio merge es mejor que insertion para n = 120. <br>\n",
    "Se tomara K = 120 para hacer la funcion hibrida de insertion y merge que se llamara \" Combined Sort \"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 ('Merge: ', 4.150871446213955e-05, ' Insertion: ', 1.4692861172420634e-05, ' Combined: ', 7.85961488304565e-06)\n",
      "20 ('Merge: ', 0.00014693650686481877, ' Insertion: ', 3.315960071063273e-05, ' Combined: ', 2.330646221409438e-05)\n",
      "30 ('Merge: ', 0.00014220336862067026, ' Insertion: ', 4.170609303741913e-05, ' Combined: ', 4.433517566496903e-05)\n",
      "40 ('Merge: ', 0.00019174144354053621, ' Insertion: ', 7.37998494390979e-05, ' Combined: ', 7.630655735013646e-05)\n",
      "50 ('Merge: ', 0.0002266261330025543, ' Insertion: ', 0.0001792829078438274, ' Combined: ', 9.273240241711278e-05)\n",
      "60 ('Merge: ', 0.0002408689710222234, ' Insertion: ', 0.00014951427106367986, ' Combined: ', 0.00013386609758427425)\n",
      "70 ('Merge: ', 0.00025358015129427257, ' Insertion: ', 0.00017476688603338176, ' Combined: ', 0.00018000531343091095)\n",
      "80 ('Merge: ', 0.0003437742652289444, ' Insertion: ', 0.00021578610162691802, ' Combined: ', 0.00023218826126466746)\n",
      "90 ('Merge: ', 0.0003854566728368525, ' Insertion: ', 0.0003162754820675673, ' Combined: ', 0.0003601685297242341)\n",
      "100 ('Merge: ', 0.000404191847238593, ' Insertion: ', 0.0003157030841984465, ' Combined: ', 0.00031233580569761443)\n",
      "110 ('Merge: ', 0.00045883807969602223, ' Insertion: ', 0.00040156276461075893, ' Combined: ', 0.00040580245641592684)\n",
      "120 ('Merge: ', 0.0005355512369119707, ' Insertion: ', 0.0005819273070495968, ' Combined: ', 0.0005502598883703059)\n",
      "130 ('Merge: ', 0.0006562008650703888, ' Insertion: ', 0.0006204240244458958, ' Combined: ', 0.0005617354787594309)\n",
      "140 ('Merge: ', 0.000620120061439451, ' Insertion: ', 0.000657365398667622, ' Combined: ', 0.0005924870608474465)\n",
      "150 ('Merge: ', 0.0008786386246976008, ' Insertion: ', 0.0008674827876009771, ' Combined: ', 0.0006208977330283005)\n",
      "160 ('Merge: ', 0.0006857208048474206, ' Insertion: ', 0.0011155126533491, ' Combined: ', 0.0007252715238375629)\n",
      "170 ('Merge: ', 0.0007733924205835763, ' Insertion: ', 0.0010422654639205575, ' Combined: ', 0.0007406473148814997)\n",
      "180 ('Merge: ', 0.0007410183866034004, ' Insertion: ', 0.001045857753997268, ' Combined: ', 0.0007128090405700505)\n",
      "190 ('Merge: ', 0.0007535321883003121, ' Insertion: ', 0.0011292462546427374, ' Combined: ', 0.0007490240616326105)\n",
      "200 ('Merge: ', 0.0007689198220592174, ' Insertion: ', 0.0012852148051301527, ' Combined: ', 0.0007816941634763453)\n"
     ]
    }
   ],
   "source": [
    "def combinedSort(A):\n",
    "    if len(A) < 120:\n",
    "        insertionSort(A)\n",
    "    else:\n",
    "        mergeSort(A)\n",
    "\n",
    "def combinedCase(A):\n",
    "    combinedTimes = []\n",
    "    gc.collect()\n",
    "    for i in xrange(10):\n",
    "        B = list(A)\n",
    "        t1 = time.clock()\n",
    "        combinedSort(B)\n",
    "        t2 = time.clock() - t1\n",
    "        combinedTimes.append(t2)\n",
    "    return arrAverage(combinedTimes)\n",
    "\n",
    "def averageCase3(n):\n",
    "    mergeTimes = []\n",
    "    insertionTimes = []\n",
    "    combinedTimes = []\n",
    "    for i in xrange(10):\n",
    "        A = randList(n)\n",
    "        random.shuffle(A)\n",
    "        mergeTimes.append(mergeCase(A))\n",
    "        insertionTimes.append(insertionCase(A))\n",
    "        combinedTimes.append(combinedCase(A))\n",
    "    return \"Merge: \",arrAverage(mergeTimes),\" Insertion: \",arrAverage(insertionTimes),\\\n",
    "           \" Combined: \",arrAverage(combinedTimes)\n",
    "\n",
    "casos = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]\n",
    "for i in casos:\n",
    "    print i, averageCase3(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Grafica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.text.Text at 0x7af90b8>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x786c588>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Modifico averageCase para poder obtener los tiempos y poder graficarlos\n",
    "def averageCase4(n,arrayM,arrayI,arrayC,arrayN):\n",
    "    arrayN.append(n)\n",
    "    mergeTimes = []\n",
    "    insertionTimes = []\n",
    "    combinedTimes = []\n",
    "    for i in xrange(10):\n",
    "        A = randList(n)\n",
    "        random.shuffle(A)\n",
    "        mergeTimes.append(mergeCase(A))\n",
    "        insertionTimes.append(insertionCase(A))\n",
    "        combinedTimes.append(combinedCase(A))\n",
    "    arrayM.append(arrAverage(mergeTimes))\n",
    "    arrayI.append(arrAverage(insertionTimes))\n",
    "    arrayC.append(arrAverage(combinedTimes))\n",
    "    \n",
    "graphMerge = []\n",
    "graphInsertion = []\n",
    "graphCombined = []\n",
    "NS = []\n",
    "\n",
    "for size in xrange(30,200,10):\n",
    "    averageCase4(size, graphMerge, graphInsertion, graphCombined, NS)\n",
    "    \n",
    "import math\n",
    "import numpy as np\n",
    "import pylab as pl\n",
    "%matplotlib inline\n",
    "pl.clf()\n",
    "pl.plot(np.array(NS),np.array(graphMerge),'Y', label= \"Merge Sort\")\n",
    "pl.plot(np.array(NS),np.array(graphInsertion),'B', label = \"Insertion Sort\")\n",
    "pl.plot(np.array(NS),np.array(graphCombined),'R', label = \"Combined Sort\")\n",
    "pl.legend(loc = \"upper left\")\n",
    "pl.xlabel(\"Array Size\")\n",
    "pl.ylabel(\"time (s)\")\n",
    "pl.title('Comparacion de Insertion, Merge y Combined')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En la grafica se puede ver como la aproximacion del K fue muy buena para lograr que el algoritmo \"Combinado\" sea eficiente para cualquier tamaño de arreglo."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
Status API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Contact Help