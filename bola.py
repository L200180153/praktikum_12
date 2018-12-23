def hitungluas(r) :
    "fungsi menghitung luas bola"
    L =  4*3.14*r**2
    return L

print '<!DOCTYPE hhtml>'
print
print'''<html>
<head> <title> Bangun Geometri </title></head>'''

print '''<body> <table> <tr>
        <td> <img src='bola.jpeg' width='100' height='150'></td>
        <td> <h1> Bangun Geometri </h1>'''
print   'Nama Bangun :  Bola <br>'
print   'Dimensi : 3D <br>'
print   'Rumus Luas: 4x3.14xrxr<br>'
print   'r : 15<br>'
print   'Luas :'
print hitungluas(15)
print ''' cm^2</td></tr></table>'''
print'</body></html>'
        
