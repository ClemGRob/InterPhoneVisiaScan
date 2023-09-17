# Utilisation du programme QML et Python

Ce programme illustre l'interaction entre QML et Python en utilisant PyQt. Il vous permet d'envoyer et de recevoir du texte ainsi que des actions entre les deux langages.

## Partie QML

- Pour récupérer un texte, déclarez un Label dans votre fichier QML :
  ```qml
  Label {
      id: lbl2
      objectName: 'pyLbl2'
      text: "unset"
  }```
Pour envoyer un message vers Python, déclarez un Label :

```qml
Label {
    id: lbl1
    objectName: 'pyLbl1'
    text: "texte provenant du fichier qml"
}```
Pour transmettre une action via un clic, utilisez un Button :

```qml
Button {
    text: 'Appuyez'
    onClicked: backend.sendEvent('Second texte provenant du fichier qml')
}```

Partie Python
Dans la partie principale de votre programme Python, définissez le contexte :

Récupération de l'evenenemt dans le main doit etre présent:
```python
context = view.rootContext()
context.setContextProperty("backend", backend)
```

Pour transmettre un texte depuis Python vers QML, utilisez :
```python
backend.transmit_textonQML("Texte depuis Python", "pyLbl2")
```

Pour recevoir un message depuis QML dans Python :
```python
label_name = "pyLbl1"
text_retour = backend.receive_textonPYTHON(label_name)
print("Texte reçu sur Python:", text_retour)
```
