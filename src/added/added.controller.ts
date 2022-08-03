import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
} from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { AddedService } from './added.service';
import { CreateAddedDto } from './dto/create-added.dto';
import { UpdateAddedDto } from './dto/update-added.dto';

@ApiTags('Added')
@Controller('added')
export class AddedController {
  constructor(private readonly addedService: AddedService) {}

  @Post()
  create(@Body() createAddedDto: CreateAddedDto) {
    return this.addedService.create(createAddedDto);
  }

  @Get()
  findAll() {
    return this.addedService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.addedService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateAddedDto: UpdateAddedDto) {
    return this.addedService.update(+id, updateAddedDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.addedService.remove(+id);
  }
}
