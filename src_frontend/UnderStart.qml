import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Rectangle {
    width: Constants.fullscreenWidth * 0.5
    height: Constants.fullscreenHeight * 0.8
    color: "transparent"
    
    signal onClicked()
    
    Rectangle {
        width: parent.width
        height: parent.height
        color: "transparent"
        Label {
            visible:false
            id: lbcustom
            objectName: 'pyLbcustom'
            text: ""
        }

        Text {
            id: titreprojet
            x: parent.width * 0.2
            y: parent.height * 0.10
            width: parent.width *0.7
            height: parent.height * 0.2
            color: Constants.colorblanc
            text: qsTr(Constants.textenameprojet)
            font.pixelSize: 80
            horizontalAlignment: Text.AlignHCenter
            anchors.topMargin: 5
        }

        Text {
            id: soustitreprojet1
            x: parent.width * 0.2
            y: parent.height * 0.25
            width: parent.width *0.7
            height: parent.height * 0.2
            color: Constants.colorblanc
            text: qsTr(Constants.texteprojet)
            font.pixelSize: 50
            horizontalAlignment: Text.AlignHCenter
            anchors.verticalCenterOffset: 7
            anchors.topMargin: 6
        }

        Text {
            id: soustitreprojet2
            x: parent.width * 0.2
            y: parent.height * 0.35
            width: parent.width *0.7
            height: parent.height * 0.2
            color: Constants.colorblanc
            text: qsTr(Constants.texteprojet_gene)
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
            anchors.leftMargin: 105
            anchors.rightMargin: 115
            anchors.horizontalCenter: soustitreprojet1.horizontalCenter
            anchors.topMargin: 5
            anchors.verticalCenterOffset: 50
        }

        Text {
            visible: false
            id: lbmiddle
            objectName: 'pyLbmiddle'
        anchors.centerIn: parent
        property string content1 : "Please, place your face in front the device. \n\n"
        property string content2 : "You can swipe to the right and to the left \n\n"
        property string content3 : "                   <--- & --->\n\n\n\n\n\n"
        property string content4 : "                    " + lbcustom.text
        text: content1 + content2 + content3+content4
        }
    }
}