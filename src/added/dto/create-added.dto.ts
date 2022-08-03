import { ApiProperty } from '@nestjs/swagger';

export class CreateAddedDto {
  @ApiProperty()
  id: number;
  @ApiProperty()
  name: string;
  @ApiProperty()
  price: number;
  @ApiProperty()
  available: boolean;
  @ApiProperty()
  Base: number;
}
