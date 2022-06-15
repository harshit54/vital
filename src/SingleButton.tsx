import {
  BsFillMouseFill,
  BsFillKeyboardFill,
  BsFillChatLeftDotsFill,
  BsWindows,
  BsPause,
} from "react-icons/bs";

import { RiArrowUpDownFill } from "react-icons/ri";
import { MdAdsClick } from "react-icons/md";
import { IoMdLocate } from "react-icons/io";
import { FiSettings } from "react-icons/fi";
import { CgScrollV } from "react-icons/cg";
import { TbSubtask } from "react-icons/tb";
import { BiErrorCircle } from "react-icons/bi";

interface SingleButtonProps {
  iconName: iconNameEnum;
}

export enum iconNameEnum {
  reposition,
  leftClick,
  rightClick,
  preciseMouse,
  scroll,
  keyboard,
  textToSpeech,
  startMenu,
  taskView,
  launchCallibration,
  eyeControlSettings,
  pauseControl,
  error,
}

export default function SingleButton(props: SingleButtonProps) {
  let icon = <RiArrowUpDownFill />;
  switch (props.iconName) {
    case iconNameEnum.reposition:
      icon = <RiArrowUpDownFill />;
      break;
    case iconNameEnum.leftClick:
      icon = <MdAdsClick className="rotate-90" />;
      break;
    case iconNameEnum.rightClick:
      icon = <MdAdsClick />;
      break;
    case iconNameEnum.preciseMouse:
      icon = <BsFillMouseFill />;
      break;
    case iconNameEnum.scroll:
      icon = <CgScrollV />;
      break;
    case iconNameEnum.keyboard:
      icon = <BsFillKeyboardFill />;
      break;
    case iconNameEnum.textToSpeech:
      icon = <BsFillChatLeftDotsFill />;
      break;
    case iconNameEnum.startMenu:
      icon = <BsWindows />;
      break;
    case iconNameEnum.taskView:
      icon = <TbSubtask />;
      break;
    case iconNameEnum.launchCallibration:
      icon = <IoMdLocate />;
      break;
    case iconNameEnum.eyeControlSettings:
      icon = <FiSettings />;
      break;
    case iconNameEnum.pauseControl:
      icon = <BsPause />;
      break;
    case iconNameEnum.error:
      icon = <BiErrorCircle />;
      break;
    default:
      icon = <BiErrorCircle />;
      break;
  }

  return (
    <div className="w-fit bg-gray-900 text-white text-5xl p-8 hover:bg-slate-600 content-center">
      {icon}
    </div>
  );
}
