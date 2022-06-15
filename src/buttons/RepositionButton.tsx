import {
  AbstractButtonProps,
  ButtonClass,
  ButtonLayout,
} from "./AbstractButton";
import { RiArrowUpDownFill } from "react-icons/ri";
import { window } from "@tauri-apps/api";
import { LogicalPosition } from "@tauri-apps/api/window";

class RepositionButtonProps extends AbstractButtonProps {
  callback() {
    console.log("Hello");
    window.getCurrent().setPosition(new LogicalPosition(100, 200));
  }
}

const RepositionButtonLayout = new ButtonLayout(<RiArrowUpDownFill />);

const RepositionButton = new ButtonClass(
  new RepositionButtonProps(),
  RepositionButtonLayout
);

export { RepositionButton };
