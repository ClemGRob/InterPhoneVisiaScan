import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Rectangle {
    width: Constants.fullscreenWidth * 0.5
    height: Constants.fullscreenHeight * 0.8
    color: "transparent"

    signal onClicked()

    Rectangle {
        id: rectanglemain1
        x: 0
        y: 0
        width: parent.width
        height: parent.height
        color: "#2b678f"
        radius: 5
        Rectangle {
            id: rectangle15
            x: parent.width * 0.03
            y: parent.height * 0.015
            width: parent.width *0.45
            height: parent.height * 0.97
            color: "#004aac"
            radius: 5             
            RoundButton {
                id: myRoundButtonAppeladmin
                x: parent.width * 0.015
                y: parent.height * 0.015
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Open Admin"
                    color: "#ffffff"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonAppeladmin.radius = 5
                    color: "#007acc"
                }
                //onPressed: parent.color =  Constants.colorbleufoncé
                //onReleased: parent.color = Constants.colorbleu
                onClicked:{ 
                    backend.handleButtonPress("Open_Admin")
                }
            }
            RoundButton {
                id: myRoundButtonAppelclose
                x: parent.width * 0.015
                y: parent.height * 0.135
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Close windows"
                    color: "#ff0000"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonAppelclose.radius = 5
                    color: "#007acc"
                }
                onClicked:{
                    backend.handleButtonPress("Close_UI")
                    Qt.quit()
                }
            }

            RoundButton {
                id: myRoundButtonopenlog
                x: parent.width * 0.015
                y: parent.height * 0.255
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Refresh log"
                    color: "#ffffff"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonopenlog.radius = 5
                    color: "#007acc"
                }
                onClicked:{
                    logTextArealog.text = "sdsdfsdfsdfsf"
                }
            }

            RoundButton {
                id: myRoundButtonopenlogadmin
                x: parent.width * 0.015
                y: parent.height * 0.375
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Refresh Admin log"
                    color: "#ffffff"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonopenlogadmin.radius = 5
                    color: "#007acc"
                }
                onClicked:{
                    // Charger le contenu du fichier .log ici
                    var file = Qt.resolvedUrl("chemin/vers/votre/fichier.log");
                    var fileContent = "";

                    // Lire le contenu du fichier
                    if (file !== "") {
                        var fileHandle = new XMLHttpRequest();
                        fileHandle.open("GET", file, false);
                        fileHandle.send(null);
                        if (fileHandle.status === 200) {
                            fileContent = fileHandle.responseText;
                        }
                    }

                    // Afficher le contenu dans la zone de texte
                    logTextArealogadmin.text = fileContent
                }
            }

            RoundButton {
                id: myRoundButtonAppeltest
                x: parent.width * 0.015
                y: parent.height * 0.495
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Open Test"
                    color: "#00FF00"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonAppeltest.radius = 5
                    color: "#007acc"
                }
                //onPressed: parent.color =  Constants.colorbleufoncé
                //onReleased: parent.color = Constants.colorbleu
                onClicked:{ 
                    backend.handleButtonPress("Open_Test")
                }
            }

            RoundButton {
                id: myRoundButtonRESTadmin
                x: parent.width * 0.015
                y: parent.height * 0.615
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "close access admin"
                    color: "#aa0000"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonRESTadmin.radius = 5
                    color: "#007acc"
                }
                //onPressed: parent.color =  Constants.colorbleufoncé
                //onReleased: parent.color = Constants.colorbleu
                onClicked:{ 
                    backend.handleButtonPress("Block_admin")
                }
            }

            RoundButton {
                id: myRoundButtonReboot
                x: parent.width * 0.015
                y: parent.height * 0.735
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Reboot application"
                    color: "#0000aa"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonReboot.radius = 5
                    color: "#007acc"
                }
                //onPressed: parent.color =  Constants.colorbleufoncé
                //onReleased: parent.color = Constants.colorbleu
                onClicked:{ 
                    backend.handleButtonPress("Reboot_app")
                }
            }
        }


        Rectangle {
            id: rectanglelog
            x: parent.width * 0.5
            y: parent.height * 0.015
            width: parent.width *0.49
            height: parent.height * 0.48
            color: "#004aac"
            radius: 5  

            Rectangle {
                color: "transparent"
                anchors.fill: parent
                Rectangle {
                    x: parent.width * 0.02
                    y: parent.height * 0.02
                    width: parent.width *0.96
                    height: parent.height * 0.96
                    color: "white"
                    TextArea {
                            id: logTextArealog
                            anchors.fill: parent
                            readOnly: true
                    }
                }
            }
        }

        Rectangle {
            id: rectanglelogadmin
            x: parent.width * 0.5
            y: parent.height * 0.5
            width: parent.width *0.49
            height: parent.height * 0.48
            color: "#004aac"
            radius: 5  
            Rectangle {
                color: "transparent"
                anchors.fill: parent
                Rectangle {
                    x: parent.width * 0.02
                    y: parent.height * 0.02
                    width: parent.width *0.96
                    height: parent.height * 0.96
                    color: "white"
                    TextArea {
                        id: logTextArealogadmin
                        anchors.fill: parent
                        readOnly: true
                    }
                }
            }
        }
    }
}