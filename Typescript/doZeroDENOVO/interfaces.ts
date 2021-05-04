export interface Pessoa {
  nome?: string,
  idade?: number,
  readonly cpf?: number;
}

export interface RecebeStringERetornaString {
  (fname: string, lname: string): string
}

export interface RelogioInterface {
  hora: Date
}