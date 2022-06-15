import { IconType } from "react-icons";
import vitalConfig from "../vitalConfig.json";

abstract class AbstractButtonProps {
  timer: any;
  abstract callback(): void;
  startTimer() {
    this.timer = setTimeout(() => {
      this.callback();
    }, vitalConfig.dwellTime * 1000);
  }
  clearTimer() {
    clearTimeout(this.timer);
  }
}

class ButtonLayout {
  icon: JSX.Element;
  constructor(icon: JSX.Element) {
    this.icon = icon;
  }
  setIcon(icon: JSX.Element) {
    this.icon = icon;
  }
}

class ButtonClass {
  props: AbstractButtonProps;
  layout: ButtonLayout;
  constructor(props: AbstractButtonProps, layout: ButtonLayout) {
    this.props = props;
    this.layout = layout;
  }
  HoverButton() {
    return (
      <div className="w-fit bg-gray-900 text-white text-5xl p-8 hover:bg-slate-600 content-center">
        <div
          onMouseEnter={this.props.startTimer}
          onMouseLeave={this.props.clearTimer}
          onClick={this.props.callback}
        >
          {this.layout.icon}
        </div>
      </div>
    );
  }
}

export { ButtonClass, ButtonLayout, AbstractButtonProps };
