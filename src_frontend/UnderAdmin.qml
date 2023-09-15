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
                x: parent.width * 0.03
                y: parent.height * 0.015
                width: parent.width * 0.95
                height: parent.height *0.1
                Text {
                    text: "Open Admin"
                    color: "#ffffff"
                    font.pixelSize: 16
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
            }/*
            RoundButton {
                id: myRoundButtonAppelclose
                x: parent.width * 0.3
                y: parent.height * 0.215
                width: parent.width * 0.95
                height: parent.height *0.1
                
                Image {
                id: poweron
                x: Constants.fullscreenWidth * 0.12
                y: Constants.fullscreenHeight * 0.09
                width: Constants.fullscreenWidth * 0.15
                height: Constants.fullscreenHeight * 0.15
                rotation: 270
                source: "Images/power-on.png"
                fillMode: Image.PreserveAspectFit

                    Text {
                        text: "Close windows"
                        color: "#ffffff"
                        font.pixelSize: 16
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.centerIn: parent
                    }
                    background: Rectangle {
                        radius: myRoundButtonAppeladmin.radius = 5
                        color: "#007acc"
                    }
                    onPressed: parent.color =  Constants.colorbleufoncé
                    onReleased: parent.color = Constants.colorbleu
                    onClicked:{ 
                        backend.handleButtonPress("Close_window")

                    }
                }
            }*/
        }
    }
}   