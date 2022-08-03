import { ApiProperty } from '@nestjs/swagger';
import { CreateAddedDto } from '../../added/dto/create-added.dto';

export class CreateBaseDto {
  @ApiProperty()
  id: number;
  @ApiProperty()
  name: string;
  @ApiProperty()
  price: number;
  @ApiProperty()
  available: boolean;
  @ApiProperty()
  addeds: CreateAddedDto[];
}
