import { IFormEvent } from "@/helpers/interfaces/events/index";

export const frozen = (event: IFormEvent) => {
  event.preventDefault();
};
