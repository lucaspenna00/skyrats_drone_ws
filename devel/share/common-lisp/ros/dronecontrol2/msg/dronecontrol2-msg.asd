
(cl:in-package :asdf)

(defsystem "dronecontrol2-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Vector3D" :depends-on ("_package_Vector3D"))
    (:file "_package_Vector3D" :depends-on ("_package"))
  ))