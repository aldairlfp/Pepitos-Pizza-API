import { Base } from '../entities/base.entity';
import { AppDataSource } from '../../main';

export class BaseRepository {
  baseRepository = AppDataSource.manager.getRepository(Base);

  async findAll(): Promise<Base[]> {
    return await this.baseRepository.find();
  }

  async findOne(id: number): Promise<Base> {
    return await this.baseRepository.findOneBy({ id: id });
  }

  async create(base: Base): Promise<Base> {
    await AppDataSource.manager.save(base);
    return base;
  }

  async update(base: Base, newBase: Base): Promise<Base> {
    base.name = newBase.name;
    base.available = newBase.available;
    base.price = newBase.price;
    const updatedBase = await this.baseRepository.save(newBase);

    return updatedBase;
  }

  async remove(id: number): Promise<Base> {
    const base = await this.baseRepository.findOneBy({ id: id });
    base.available = false;
    const removedBase = await this.baseRepository.save(base);
    return removedBase
  }
}
