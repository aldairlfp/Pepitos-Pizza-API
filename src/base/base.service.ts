import { Injectable } from '@nestjs/common';
import { CreateBaseDto } from './dto/create-base.dto';
import { UpdateBaseDto } from './dto/update-base.dto';
import { Base } from './entities/base.entity';
import { BaseRepository } from './repositories/base.repository';

@Injectable()
export class BaseService {
  constructor(private baseRepository: BaseRepository) {}

  async create(createBaseDto: CreateBaseDto): Promise<Base> {
    const newBase = { ...createBaseDto };

    const base = new Base();

    base.name = newBase.name;
    base.price = newBase.price;
    base.available = newBase.available;

    const createdBase = await this.baseRepository.create(base);

    return createdBase;
  }

  async findAll(): Promise<Base[]> {
    return await this.baseRepository.findAll();
  }

  async findOne(id: number): Promise<Base> {
    return await this.baseRepository.findOne(id);
  }

  async update(id: number, updateBaseDto: UpdateBaseDto): Promise<Base> {
    const oldBase = await this.findOne(id)
    const newBase = new Base()

    newBase.id = updateBaseDto.id ? updateBaseDto.id : oldBase.id
    newBase.name = updateBaseDto.name ? updateBaseDto.name : oldBase.name
    newBase.available = updateBaseDto.available ? updateBaseDto.available : oldBase.available
    newBase.price = updateBaseDto.price ? updateBaseDto.price : oldBase.price

    const updatedBase = await this.baseRepository.update(oldBase, newBase)

    return updatedBase
  }

  async remove(id: number): Promise<Base> {
    const base = await this.baseRepository.remove(id)
    return base
  }
}
