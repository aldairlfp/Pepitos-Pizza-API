import { ApiProperty } from '@nestjs/swagger';
import { type } from 'os';
import { Added } from 'src/added/entities/added.entity';
import { Column, Entity, PrimaryColumn, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Base {
  @ApiProperty()
  @PrimaryGeneratedColumn()
  id: number;

  @ApiProperty()
  @Column({ length: 100, unique: true })
  name: string;

  @ApiProperty()
  @Column('double')
  price: number;

  @ApiProperty()
  @Column()
  available: boolean;
}
