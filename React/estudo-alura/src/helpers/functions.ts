import { IFormEvent } from "@/components/public/interfaces/events/form";

export const frozen = (event: IFormEvent) => {
  event.preventDefault();
};
