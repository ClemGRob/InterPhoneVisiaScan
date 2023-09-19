import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

SwipeView {
    property int currentPage: 1
    property int limitewithshow: parent.width
    property int limiteheightshow: parent.height

    id: swipeView
    width: Math.min(limitewithshow,limitewithshow-1)
    height: Math.min(limiteheightshow,limiteheightshow-1)
    currentIndex: currentPage   
    
    Item{
        visible: currentIndex === 0
        Rectangle {
            id: rectangleUnderDefilement
            x: 0
            y: 0
            width: parent.width
            height: parent.height
            color: Constants.colorblanc 
            Rectangle {
                width: swipeView.width
                height: swipeView.height
                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: {
                        backend.handleButtonPress("Select_interface Display Numeric keypad")
                    }
                    UnderNumericKeypad {}
                }
            }
        }
    }

    Item{
        visible: currentIndex === 1 
        Rectangle {
            width: swipeView.width
            height: swipeView.height
            color: "transparent"

            MouseArea {
                width: parent.width
                height: parent.height
                onClicked: {
                    backend.handleButtonPress("Select_interface Menu")
                }
                UnderStart {}
            }
        }
    }

    Item {
        visible: currentIndex === 2
        Rectangle {
            width: swipeView.width
            height: swipeView.height
            color: "transparent"

            MouseArea {
                width: parent.width
                height: parent.height
                onClicked: {
                    backend.handleButtonPress("Select_interface Display Search Hab")
                }
                UnderSearch{}
            }
        }
    }

    Item {
        visible: currentIndex === 3 && lbcurrentLabelvisible.text === "Code bon"
        Rectangle {
            id :rectangleAdmin
            width: swipeView.width
            height: swipeView.height

            Label {
                id: lbcurrentLabelvisible
                objectName: 'pyLcurrentLabelvisible'
                text: ""
                visible: false
                onTextChanged: {
                    if (lbcurrentLabelvisible.text === "Code bon") {
                        rectangleAdmin.visible = true
                    } else {
                        rectangleAdmin.visible = false
                    }
                }
            }

            visible: lbcurrentLabelvisible.text === "Code bon"
            MouseArea {
                width: parent.width
                height: parent.height
                onClicked: {
                    backend.handleButtonPress("Select_interface Display Admin")
                }
            }
            UnderAdmin {}
        }
    }  
}