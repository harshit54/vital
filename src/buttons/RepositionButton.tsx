import {
  AbstractButtonProps,
  ButtonClass,
  ButtonLayout,
} from "./AbstractButton";
import { RiArrowUpDownFill } from "react-icons/ri";
import { window } from "@tauri-apps/api";
import { LogicalPosition } from "@tauri-apps/api/window";

class RepositionButtonProps extends AbstractButtonProps {
  async callback() {
    console.log("Hello");
    let size = await window.primaryMonitor();
    console.log(size);
    let resX = size?.size.width,
      resY = size?.size.height;
    let size2 = await window.getCurrent().outerSize();
    let currX = size2.width,
      currY = size2.height;

    window
      .getCurrent()
      .setPosition(new LogicalPosition(Math.floor(resX! / 2 - currX! / 2), 0));
  }
}

const RepositionButtonLayout = new ButtonLayout(<RiArrowUpDownFill />);

const RepositionButton = new ButtonClass(
  new RepositionButtonProps(),
  RepositionButtonLayout
);

export { RepositionButton };
