import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Rectangle {
    width: Constants.fullscreenWidth * 0.5
    height: Constants.fullscreenHeight * 0.8
    color: "#aaaaaa"

    signal onClicked()
        
    Rectangle {
        id: rectanglemain1
        x: parent.width * 0.025
        y: parent.height * 0.02
        width: parent.width * 0.95
        height: parent.height * 0.235
        color: "#2b678f"
        radius: 5
        Rectangle {
            id: rectangle15
            x: parent.width * 0.3
            y: parent.height * 0.05
            width: parent.width * 0.37
            height: parent.height * 0.9
            color: "#007acc"
            radius: 5
            Rectangle {
                id: rectangleText
                x: 5
                y: 5
                width: parent.width - 10
                height: parent.height - 10
                color: "#000000"
                radius: 5
                Text {
                    id: lbNum_Keypad
                    objectName: 'pyLbNum_Keypad'
                    width: parent.width
                    height: parent.height
                    color: "#ffffff"
                    text: "Waiting code PIN"
                    font.pixelSize: 30
                    verticalAlignment: Text.AlignVCenter
                    anchors.verticalCenterOffset: 0
                    anchors.horizontalCenterOffset: 0
                    anchors.centerIn: parent
                }
            }
        }
        RoundButton {
            id: myRoundButtonC
            x: parent.width * 0.025
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "C"
                color: "#ff0000"
                font.pixelSize: 60
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonC.radius = 5
                color: Constants.colorrouge
            } 
            onPressed: {
                myRoundButtonC.background.color = Constants.colorrougefoncé;
            }
            onReleased: {
                myRoundButtonC.background.color = Constants.colorrouge;
            }         
            onClicked: {
                backend.handleButtonPress("C")
            }
        }
            
        RoundButton {
            id: myRoundButtonV
            x: parent.width * 0.7
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "V"
                color: "#00FF00"
                font.pixelSize: 60
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonC.radius = 5
                color: "#00ac7a"
            }
            onPressed: {
                myRoundButtonV.background.color = Constants.colorvertfoncé;
            }
            onReleased: {
                myRoundButtonV.background.color = Constants.colorvert;
            }
            onClicked: {
                backend.handleButtonPress("V")
            }
        }
    }

    Rectangle {
        id: rectanglemain2
        x: parent.width * 0.025
        y: parent.height * 0.275
        width: parent.width * 0.95
        height: parent.height / 6
        color: "#2b678f"
        radius: 5

        RoundButton {
            id: myRoundButton1
            x: parent.width * 0.075
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "1"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton1.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton1.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton1.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("1")
            }
        }

        RoundButton {
            id: myRoundButton2
            x: parent.width * 0.375
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "2"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton2.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton2.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton2.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("2")
            }
        }

        RoundButton {
            id: myRoundButton3
            x: parent.width * 0.675
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "3"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton3.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton3.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton3.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("3")
            }
        }
    }

    Rectangle {
        id: rectanglemain3
        x: parent.width * 0.025
        y: parent.height * 0.455
        width: parent.width * 0.95
        height: parent.height / 6
        color: "#2b678f"
        radius: 5
        RoundButton {
            id: myRoundButton4
            x: parent.width * 0.075
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "4"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton4.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton4.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton4.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("4")
            }
        }

        RoundButton {
            id: myRoundButton5
            x: parent.width * 0.375
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "5"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton5.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton5.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton5.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("5")
            }
        }

        RoundButton {
            id: myRoundButton6
            x: parent.width * 0.675
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "6"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton6.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton6.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton6.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("6")
            }
        }
    }

    Rectangle {
        id: rectanglemain4
        x: parent.width * 0.025
        y: parent.height * 0.635
        width: parent.width * 0.95
        height: parent.height / 6
        color: "#2b678f"
        radius: 5

        RoundButton {
            id: myRoundButton7
            x: parent.width * 0.075
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "7"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton7.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton7.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton7.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("7")
            }
        }

        RoundButton {
            id: myRoundButton8
            x: parent.width * 0.375
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "8"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton8.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton8.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton8.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("8")
            }
        }

        RoundButton {
            id: myRoundButton9
            x: parent.width * 0.675
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "9"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton9.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton9.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton9.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("9")
            }
        }   
    }

    Rectangle {
        id: rectanglemain5
        x: parent.width * 0.025
        y: parent.height * 0.815
        width: parent.width * 0.95
        height: parent.height / 6
        color: "#2b678f"
        radius: 5
        
        RoundButton {
            id: myRoundButtondiez
            x: parent.width * 0.075
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "#"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtondiez.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButtondiez.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButtondiez.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("#")
            }
        }

        RoundButton {
            id: myRoundButton0
            x: parent.width * 0.375
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "0"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton0.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButton0.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButton0.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("0")
            }
        }

        RoundButton {
            id: myRoundButtonetoile
            x: parent.width * 0.675
            y: parent.height * 0.2
            width: parent.width * 0.25
            height: parent.height * 0.6
            Text {
                text: "*"
                color: "#ffffff"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonetoile.radius = 5
                color: "#007acc"
            }
            onPressed: {
                myRoundButtonetoile.background.color = Constants.colorbleufoncé;
            }
            onReleased: {
                myRoundButtonetoile.background.color = Constants.colorbleu;
            }
            onClicked: {
                backend.handleButtonPress("*")
            }
        }  
    }
}