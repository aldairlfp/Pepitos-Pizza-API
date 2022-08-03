import { PartialType } from '@nestjs/mapped-types';
import { CreateAddedDto } from './create-added.dto';

export class UpdateAddedDto extends PartialType(CreateAddedDto) {}
