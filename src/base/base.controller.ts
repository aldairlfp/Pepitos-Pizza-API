import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  Req,
} from '@nestjs/common';
import { ApiCreatedResponse, ApiTags } from '@nestjs/swagger';
import { BaseService } from './base.service';
import { CreateBaseDto } from './dto/create-base.dto';
import { UpdateBaseDto } from './dto/update-base.dto';
import { Base } from './entities/base.entity';

@ApiTags('Base')
@Controller('base')
export class BaseController {
  constructor(private readonly baseService: BaseService) {}

  @ApiCreatedResponse({ type: Base })
  @Post()
  async create(@Body() createBaseDto: CreateBaseDto): Promise<Base> {
    return this.baseService.create(createBaseDto);
  }

  @Get()
  async findAll(): Promise<Base[]> {
    return this.baseService.findAll();
  }

  @Get(':id')
  async findOne(@Param('id') id: string): Promise<Base> {
    return this.baseService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateBaseDto: UpdateBaseDto): Promise<Base> {
    return this.baseService.update(+id, updateBaseDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string): Promise<Base> {
    return this.baseService.remove(+id);
  }
}
