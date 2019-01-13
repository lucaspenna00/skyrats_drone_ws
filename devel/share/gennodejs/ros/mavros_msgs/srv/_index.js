
"use strict";

let FileRemove = require('./FileRemove.js')
let CommandTOL = require('./CommandTOL.js')
let CommandHome = require('./CommandHome.js')
let CommandInt = require('./CommandInt.js')
let ParamPush = require('./ParamPush.js')
let SetMavFrame = require('./SetMavFrame.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let FileTruncate = require('./FileTruncate.js')
let FileChecksum = require('./FileChecksum.js')
let FileOpen = require('./FileOpen.js')
let ParamSet = require('./ParamSet.js')
let CommandLong = require('./CommandLong.js')
let ParamGet = require('./ParamGet.js')
let FileList = require('./FileList.js')
let FileMakeDir = require('./FileMakeDir.js')
let FileRename = require('./FileRename.js')
let StreamRate = require('./StreamRate.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let FileWrite = require('./FileWrite.js')
let WaypointClear = require('./WaypointClear.js')
let WaypointPush = require('./WaypointPush.js')
let CommandBool = require('./CommandBool.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let ParamPull = require('./ParamPull.js')
let SetMode = require('./SetMode.js')
let FileRead = require('./FileRead.js')
let WaypointPull = require('./WaypointPull.js')
let FileClose = require('./FileClose.js')

module.exports = {
  FileRemove: FileRemove,
  CommandTOL: CommandTOL,
  CommandHome: CommandHome,
  CommandInt: CommandInt,
  ParamPush: ParamPush,
  SetMavFrame: SetMavFrame,
  WaypointSetCurrent: WaypointSetCurrent,
  FileTruncate: FileTruncate,
  FileChecksum: FileChecksum,
  FileOpen: FileOpen,
  ParamSet: ParamSet,
  CommandLong: CommandLong,
  ParamGet: ParamGet,
  FileList: FileList,
  FileMakeDir: FileMakeDir,
  FileRename: FileRename,
  StreamRate: StreamRate,
  FileRemoveDir: FileRemoveDir,
  FileWrite: FileWrite,
  WaypointClear: WaypointClear,
  WaypointPush: WaypointPush,
  CommandBool: CommandBool,
  CommandTriggerControl: CommandTriggerControl,
  ParamPull: ParamPull,
  SetMode: SetMode,
  FileRead: FileRead,
  WaypointPull: WaypointPull,
  FileClose: FileClose,
};
