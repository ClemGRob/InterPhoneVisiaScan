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
            x: parent.width * 0.02
            y: parent.height * 0.02
            width: parent.width * 0.96
            height: parent.height * 0.4
            color: "#007acc"
            radius: 5
            Rectangle {
                id: rectangle16
                x: parent.width * 0.015
                y: parent.height * 0.04
                width: parent.width * 0.97
                height: parent.height * 0.92
                color: "#000000"
                radius: 5
                Label {
                    id: lbSerach_Hab
                    objectName: 'pyLbSerach_Hab'
                    width: parent.width
                    height: parent.height
                    color: "#ffffff"
                    text: "Wait for your choice"
                    font.pixelSize: 50
                    verticalAlignment: Text.AlignVCenter
                    anchors.verticalCenterOffset: 0
                    anchors.horizontalCenterOffset: 0
                    anchors.centerIn: parent
                }
            }
        }

        Rectangle {
            visible: false
            id: rectanglequestion
            x: parent.width * 0.02
            y: parent.height * 0.423
            width: parent.width * 0.96
            height: parent.height * 0.56
            color: "#007acc"
            radius: 5
            Rectangle {
                id: rectanglequestionsur
                x: parent.width * 0.015
                y: parent.height * 0.04
                width: parent.width * 0.97
                height: parent.height * 0.92
                color: "#000000"
                radius: 5
                Rectangle {
                    color: "#444444"
                    y: parent.width * 0.05
                    Label {
                        id: lbQuestion
                        objectName: 'pyLbQuestion'
                        width: parent.width
                        height: parent.height
                        color: "#ffffff"
                        text: "Voulez-vous autorisez la prise d'image ?"
                        font.pixelSize: 50
                        verticalAlignment: Text.AlignVCenter
                        anchors.verticalCenterOffset: 0
                        anchors.horizontalCenterOffset: 0
                        anchors.centerIn: parent
                    }
                }
                

                RoundButton {
                    id: myRoundButtonoui
                    x: parent.width * 0.02
                    y: parent.height * 0.45
                    width: parent.width * 0.3
                    height: parent.height * 0.52
                    Text {
                        text: "OUI"
                        color: "#ffffff"
                        font.pixelSize: 55
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.centerIn: parent
                    }
                    background: Rectangle {
                        radius: myRoundButtonprecedent.radius = 5
                        color: "#007acc"
                    } 
                    onClicked: {
                        backend.handleButtonPress("ValidEnvoiPicture")
                    }
                }

                RoundButton {
                    id: myRoundButtonnon
                    x: parent.width * 0.68
                    y: parent.height * 0.45
                    width: parent.width * 0.3
                    height: parent.height * 0.52
                    Text {
                        text: "NON"
                        color: "#ffffff"
                        font.pixelSize: 55
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.centerIn: parent
                    }
                    background: Rectangle {
                        radius: myRoundButtonsuivant.radius = 5
                        color: "#007acc"
                    } 
                    onClicked:{
                        backend.handleButtonPress("InValidEnvoiPicture")
                    }
                }
            }
        }

        RoundButton {
            visible: lbSerach_Hab.text !== "Wait for your choice"
            id: myRoundButtonAppel
            x: parent.width * 0.35
            y: parent.height * 0.55
            width: parent.width * 0.3
            height: parent.height * 0.3
            Text {
                text: "Call the person"
                color: "#ffffff"
                font.pixelSize: 35
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonAppel.radius = 5
                color: "#007acc"
            } 
            onClicked:{
                myRoundButtonprecedent.visible = false
                myRoundButtonsuivant.visible = false
                myRoundButtonAppel.visible = false
                rectanglequestion.visible = true

                //backend.handleButtonPress("Call the person")
               }
        }

        RoundButton {
            id: myRoundButtonprecedent
            x: parent.width * 0.02
            y: parent.height * 0.45
            width: parent.width * 0.3
            height: parent.height * 0.52
            Text {
                text: "<<<"
                color: "#ffffff"
                font.pixelSize: 55
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonprecedent.radius = 5
                color: "#007acc"
            } 
            onClicked: {
                backend.handleButtonPress("<<<")
            }
        }

        RoundButton {
            id: myRoundButtonsuivant
            x: parent.width * 0.68
            y: parent.height * 0.45
            width: parent.width * 0.3
            height: parent.height * 0.52
            Text {
                text: ">>>"
                color: "#ffffff"
                font.pixelSize: 55
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonsuivant.radius = 5
                color: "#007acc"
            } 
            onClicked:{
                backend.handleButtonPress(">>>")
            }
        }

        
    }
}   