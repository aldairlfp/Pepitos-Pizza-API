import { Injectable } from '@nestjs/common';
import { CreateAddedDto } from './dto/create-added.dto';
import { UpdateAddedDto } from './dto/update-added.dto';

@Injectable()
export class AddedService {
  create(createAddedDto: CreateAddedDto) {
    return 'This action adds a new added';
  }

  findAll() {
    return `This action returns all added`;
  }

  findOne(id: number) {
    return `This action returns a #${id} added`;
  }

  update(id: number, updateAddedDto: UpdateAddedDto) {
    return `This action updates a #${id} added`;
  }

  remove(id: number) {
    return `This action removes a #${id} added`;
  }
}
